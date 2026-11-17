"""Modelos para la información académica y personal de egresados."""

from django.conf import settings
from django.db import models
from django.db.models import Q


class Programa(models.Model):
    """Programa de formación ofertado por el Centro."""

    codigo = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=180)
    activo = models.BooleanField(default=True)

    class Meta:
        """Ordena programas por nombre."""

        ordering = ['nombre']

    def __str__(self):
        """Devuelve el código y el nombre del programa."""

        return f'{self.codigo} · {self.nombre}'


class Ficha(models.Model):
    """Ficha formativa y periodo de vigencia asociado a un programa."""

    numero = models.CharField(max_length=30, unique=True)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.PROTECT,
        related_name='fichas',
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        """Ordena fichas por número."""

        ordering = ['numero']

    def __str__(self):
        """Devuelve el número de ficha y el programa."""

        return f'{self.numero} · {self.programa.nombre}'

    @property
    def vigente(self):
        """Indica si la fecha actual está dentro de la vigencia de la ficha."""

        from django.utils import timezone

        hoy = timezone.localdate()
        return self.fecha_inicio <= hoy <= self.fecha_fin


class Egresado(models.Model):
    """Registro personal con certificación y autorización trazables."""

    class TipoDocumento(models.TextChoices):
        """Tipos de documento de identidad aceptados."""

        CEDULA = 'CC', 'Cédula de ciudadanía'
        EXTRANJERIA = 'CE', 'Cédula de extranjería'
        PERMISO = 'PEP', 'Permiso especial de permanencia'
        PASAPORTE = 'PA', 'Pasaporte'

    class Estado(models.TextChoices):
        """Estados funcionales del seguimiento al egresado."""

        PENDIENTE = 'pendiente', 'Pendiente de validación'
        VALIDADO = 'validado', 'Validado'
        SEGUIMIENTO = 'seguimiento', 'En seguimiento'
        DESACTUALIZADO = 'desactualizado', 'Desactualizado'
        INACTIVO = 'inactivo', 'Inactivo'
        NO_LOCALIZABLE = 'no_localizable', 'No localizable'

    tipo_documento = models.CharField(
        max_length=4,
        choices=TipoDocumento.choices,
        default=TipoDocumento.CEDULA,
    )
    documento = models.CharField(max_length=30, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    municipio = models.CharField(max_length=80, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.PROTECT,
        related_name='egresados',
    )
    ficha = models.ForeignKey(
        Ficha,
        on_delete=models.PROTECT,
        related_name='egresados',
    )
    fecha_certificacion = models.DateField()
    referencia_certificacion = models.CharField(max_length=100)
    fecha_egreso = models.DateField()
    certificacion_verificada = models.BooleanField(default=False)
    autorizacion_datos = models.BooleanField(default=False)
    fecha_autorizacion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=24,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        """Prioriza los registros modificados recientemente."""

        ordering = ['-actualizado_en', 'apellidos', 'nombres']

    def __str__(self):
        """Devuelve el nombre completo del egresado."""

        return f'{self.nombres} {self.apellidos}'


class Vinculacion(models.Model):
    """Historial de la relación de un egresado con una ficha formativa."""

    egresado = models.ForeignKey(
        Egresado,
        on_delete=models.PROTECT,
        related_name='vinculaciones',
    )
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT)
    ficha = models.ForeignKey(Ficha, on_delete=models.PROTECT)
    cohorte = models.CharField(max_length=20)
    activa = models.BooleanField(default=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Evita duplicar vinculaciones activas para programa y ficha."""

        constraints = [
            models.UniqueConstraint(
                fields=['egresado', 'programa', 'ficha'],
                condition=Q(activa=True),
                name='vinculacion_activa_unica',
            ),
        ]


class AccionSeguimiento(models.Model):
    """Evidencia de contacto telefónico o presencial con un egresado."""

    class Medio(models.TextChoices):
        """Canales permitidos para la gestión de seguimiento."""

        TELEFONO = 'telefono', 'Teléfono'
        PRESENCIAL = 'presencial', 'Presencial'

    egresado = models.ForeignKey(
        Egresado,
        on_delete=models.PROTECT,
        related_name='acciones_seguimiento',
    )
    funcionario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    medio = models.CharField(max_length=20, choices=Medio.choices)
    resultado = models.CharField(max_length=500)
    creada_en = models.DateTimeField(auto_now_add=True)