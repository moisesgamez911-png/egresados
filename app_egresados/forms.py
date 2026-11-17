"""Formularios validados para las operaciones de egresados."""

from django import forms
from django.db import transaction
from django.utils import timezone

from .models import Egresado, Vinculacion


class EgresadoForm(forms.ModelForm):
    """Valida los datos básicos y certificación de un nuevo egresado."""

    class Meta:
        """Define campos editables y controles del formulario."""

        model = Egresado
        fields = [
            'tipo_documento', 'documento', 'nombres', 'apellidos',
            'correo', 'telefono', 'municipio', 'programa', 'ficha',
            'referencia_certificacion', 'fecha_certificacion',
            'fecha_egreso', 'certificacion_verificada', 'autorizacion_datos',
        ]
        widgets = {
            'fecha_certificacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_egreso': forms.DateInput(attrs={'type': 'date'}),
            'certificacion_verificada': forms.CheckboxInput(),
            'autorizacion_datos': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        """Limita la ficha al programa seleccionado cuando sea posible."""

        super().__init__(*args, **kwargs)
        fichas = self.fields['ficha'].queryset.select_related('programa')
        programa_id = self.data.get('programa') or self.initial.get('programa')
        if programa_id:
            fichas = fichas.filter(programa_id=programa_id)
        self.fields['ficha'].queryset = fichas
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')
        self.fields['certificacion_verificada'].widget.attrs['class'] = 'check-input'
        self.fields['autorizacion_datos'].widget.attrs['class'] = 'check-input'

    def clean_documento(self):
        """Rechaza documentos duplicados y normaliza espacios exteriores."""

        documento = self.cleaned_data['documento'].strip()
        if Egresado.objects.filter(documento=documento).exists():
            raise forms.ValidationError(
                'Ya existe un egresado con este documento.'
            )
        return documento

    def clean_telefono(self):
        """Valida que un teléfono informado tenga al menos siete dígitos."""

        telefono = self.cleaned_data.get('telefono', '').strip()
        if telefono and sum(caracter.isdigit() for caracter in telefono) < 7:
            raise forms.ValidationError(
                'El teléfono debe tener al menos 7 dígitos.'
            )
        return telefono

    def clean(self):
        """Comprueba la certificación, fechas y relación ficha-programa."""

        datos = super().clean()
        certificacion = datos.get('fecha_certificacion')
        egreso = datos.get('fecha_egreso')
        if certificacion and egreso and egreso < certificacion:
            self.add_error(
                'fecha_egreso',
                'La fecha de egreso no puede ser anterior a la fecha de certificación.',
            )
        if certificacion and certificacion > timezone.localdate():
            self.add_error(
                'fecha_certificacion',
                'La fecha de certificación no puede estar en el futuro.',
            )
        ficha = datos.get('ficha')
        programa = datos.get('programa')
        if ficha and programa and ficha.programa_id != programa.id:
            self.add_error('ficha', 'La ficha no pertenece al programa seleccionado.')
        if not datos.get('certificacion_verificada'):
            self.add_error(
                'certificacion_verificada',
                'Confirma la verificación de la certificación antes de registrar.',
            )
        return datos

    def save(self, commit=True):
        """Registra el consentimiento con fecha y estado inicial coherente."""

        egresado = super().save(commit=False)
        if egresado.autorizacion_datos:
            egresado.fecha_autorizacion = timezone.now()
            egresado.estado = Egresado.Estado.VALIDADO
        else:
            egresado.estado = Egresado.Estado.PENDIENTE
        if commit:
            with transaction.atomic():
                egresado.save()
                self.save_m2m()
                Vinculacion.objects.create(
                    egresado=egresado,
                    programa=egresado.programa,
                    ficha=egresado.ficha,
                    cohorte=str(egresado.fecha_egreso.year),
                )
        return egresado