"""Configuración de la aplicación de egresados."""

from django.apps import AppConfig


class EgresadosConfig(AppConfig):
    """Registra la aplicación de gestión de egresados."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_egresados'
    verbose_name = 'Gestión de egresados'