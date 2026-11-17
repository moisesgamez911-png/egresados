"""Pruebas de reglas de negocio y autorización de egresados."""

from datetime import date

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from .forms import EgresadoForm
from .models import Egresado, Ficha, Programa, Vinculacion


class EgresadoFormTests(TestCase):
    """Verifica validaciones de identidad, certificación y consentimiento."""

    def setUp(self):
        """Crea un programa y ficha de prueba."""

        self.programa = Programa.objects.create(
            codigo='TEST-01',
            nombre='Programa de prueba',
        )
        self.ficha = Ficha.objects.create(
            numero='123456',
            programa=self.programa,
            fecha_inicio=date(2020, 1, 1),
            fecha_fin=date(2030, 1, 1),
        )
        self.datos = {
            'tipo_documento': Egresado.TipoDocumento.CEDULA,
            'documento': '10000001',
            'nombres': 'Ana María',
            'apellidos': 'Gómez Pérez',
            'correo': 'ana@example.com',
            'telefono': '3001234567',
            'municipio': 'Riohacha',
            'programa': str(self.programa.pk),
            'ficha': str(self.ficha.pk),
            'referencia_certificacion': 'ACTA-2024-001',
            'fecha_certificacion': '2024-03-01',
            'fecha_egreso': '2024-03-01',
            'certificacion_verificada': 'on',
            'autorizacion_datos': 'on',
        }

    def test_crea_registro_con_certificacion_y_autorizacion(self):
        """Guarda autorización y estado validado al completar los requisitos."""

        formulario = EgresadoForm(data=self.datos)

        self.assertTrue(formulario.is_valid(), formulario.errors)
        egresado = formulario.save()

        self.assertEqual(egresado.estado, Egresado.Estado.VALIDADO)
        self.assertIsNotNone(egresado.fecha_autorizacion)
        self.assertTrue(
            Vinculacion.objects.filter(
                egresado=egresado,
                programa=self.programa,
                ficha=self.ficha,
                cohorte='2024',
            ).exists()
        )

    def test_rechaza_fecha_de_egreso_anterior_a_certificacion(self):
        """Impide una fecha de egreso cronológicamente inconsistente."""

        self.datos['fecha_egreso'] = '2024-02-29'
        formulario = EgresadoForm(data=self.datos)

        self.assertFalse(formulario.is_valid())
        self.assertIn('fecha_egreso', formulario.errors)

    def test_exige_confirmar_verificacion_de_certificacion(self):
        """Impide crear registros sin confirmación de fuente certificadora."""

        self.datos.pop('certificacion_verificada')
        formulario = EgresadoForm(data=self.datos)

        self.assertFalse(formulario.is_valid())
        self.assertIn('certificacion_verificada', formulario.errors)

    def test_rechaza_documento_duplicado(self):
        """Usa el documento de identidad como identificador único."""

        Egresado.objects.create(
            tipo_documento=Egresado.TipoDocumento.CEDULA,
            documento=self.datos['documento'],
            nombres='Ana',
            apellidos='Gómez',
            programa=self.programa,
            ficha=self.ficha,
            referencia_certificacion='ACTA-ANTERIOR',
            fecha_certificacion=date(2024, 3, 1),
            fecha_egreso=date(2024, 3, 1),
            certificacion_verificada=True,
        )
        formulario = EgresadoForm(data=self.datos)

        self.assertFalse(formulario.is_valid())
        self.assertIn('documento', formulario.errors)


class EgresadoAccessTests(TestCase):
    """Comprueba la privacidad por grupos en páginas nominales."""

    def setUp(self):
        """Crea perfiles y un registro nominal de prueba."""

        self.usuario = User.objects.create_user(
            username='bienestar',
            password='test-password-123',
        )
        self.grupo = Group.objects.create(name='Visor - Bienestar al Aprendiz')
        self.usuario.groups.add(self.grupo)
        self.programa = Programa.objects.create(
            codigo='TEST-02',
            nombre='Energías renovables',
        )
        self.ficha = Ficha.objects.create(
            numero='654321',
            programa=self.programa,
            fecha_inicio=date(2020, 1, 1),
            fecha_fin=date(2030, 1, 1),
        )
        Egresado.objects.create(
            tipo_documento=Egresado.TipoDocumento.CEDULA,
            documento='10000002',
            nombres='Luis',
            apellidos='Pérez',
            programa=self.programa,
            ficha=self.ficha,
            referencia_certificacion='ACTA-2024-002',
            fecha_certificacion=date(2024, 3, 1),
            fecha_egreso=date(2024, 3, 1),
            certificacion_verificada=True,
        )
        self.client.force_login(self.usuario)

    def test_bienestar_ve_resumen_agregado_sin_datos_nominales(self):
        """Oculta personas y documentos en el panel para Bienestar."""

        respuesta = self.client.get(reverse('inicio'))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Vista agregada')
        self.assertNotContains(respuesta, '10000002')
        self.assertNotContains(respuesta, 'Luis Pérez')

    def test_bienestar_no_puede_abrir_el_directorio_nominal(self):
        """Restringe el listado nominal a perfiles autorizados."""

        respuesta = self.client.get(reverse('egresados_lista'))

        self.assertEqual(respuesta.status_code, 403)

    def test_cerrar_sesion_no_acepta_get(self):
        """Exige POST para proteger el cierre de sesión contra CSRF."""

        respuesta = self.client.get(reverse('cerrar_sesion'))

        self.assertEqual(respuesta.status_code, 405)