"""Catálogos institucionales disponibles para el superadministrador."""

from django.contrib import admin

from .models import AccionSeguimiento, Egresado, Ficha, Programa, Vinculacion


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    """Administra programas habilitados para las vinculaciones."""

    list_display = ['codigo', 'nombre', 'activo']
    list_filter = ['activo']
    search_fields = ['codigo', 'nombre']


@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    """Administra fichas y su vigencia por programa."""

    list_display = ['numero', 'programa', 'fecha_inicio', 'fecha_fin']
    list_filter = ['programa']
    search_fields = ['numero', 'programa__nombre']


@admin.register(Egresado)
class EgresadoAdmin(admin.ModelAdmin):
    """Permite al superadministrador consultar y auditar egresados."""

    list_display = ['documento', 'nombres', 'apellidos', 'programa', 'estado']
    list_filter = ['estado', 'programa', 'municipio']
    search_fields = ['documento', 'nombres', 'apellidos']
    readonly_fields = ['creado_en', 'actualizado_en', 'fecha_autorizacion']


@admin.register(Vinculacion)
class VinculacionAdmin(admin.ModelAdmin):
    """Consulta la trayectoria de formación de cada egresado."""

    list_display = ['egresado', 'programa', 'ficha', 'cohorte', 'activa']
    list_filter = ['activa', 'programa', 'cohorte']
    search_fields = ['egresado__documento', 'egresado__nombres']


@admin.register(AccionSeguimiento)
class AccionSeguimientoAdmin(admin.ModelAdmin):
    """Permite revisar acciones de seguimiento sin alterar su fecha."""

    list_display = ['egresado', 'funcionario', 'medio', 'creada_en']
    list_filter = ['medio', 'creada_en']
    search_fields = ['egresado__documento', 'resultado']
    readonly_fields = ['egresado', 'funcionario', 'medio', 'resultado', 'creada_en']