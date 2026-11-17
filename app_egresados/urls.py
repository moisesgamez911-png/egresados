"""Rutas web de la aplicación de seguimiento a egresados."""

from django.urls import path

from . import views

urlpatterns = [
    path('ingresar/', views.iniciar_sesion_view, name='iniciar_sesion'),
    path('salir/', views.cerrar_sesion_view, name='cerrar_sesion'),
    path('', views.inicio_view, name='inicio'),
    path('egresados/', views.egresados_list_view, name='egresados_lista'),
    path('egresados/nuevo/', views.egresados_create_view, name='egresado_nuevo'),
    path(
        'egresados/<int:pk>/',
        views.egresados_detail_view,
        name='egresado_detalle',
    ),
]