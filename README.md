# Seguimiento a egresados · CIEA

Aplicación web Django para la gestión y el seguimiento a egresados del Centro Industrial y de Energías Alternativas, Regional La Guajira.

## Desarrollo local

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`. El portal requiere autenticación. Entra al administrador de Django con el superusuario para crear programas y fichas. Para usuarios operativos, crea los grupos `Administrador`, `Funcionario`, `Visor - Coordinador Académico` y `Visor - Bienestar al Aprendiz`, y asigna cada cuenta al grupo correspondiente.

En despliegue, define `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false` y `DJANGO_ALLOWED_HOSTS` con los dominios permitidos. La configuración activa redirección HTTPS, HSTS y cookies seguras cuando `DJANGO_DEBUG` es `false`.

## Alcance implementado

- Acceso autenticado y restricciones por grupos de Django.
- Panel operativo responsive con indicadores y alertas.
- Búsqueda y filtros por estado y programa.
- Alta y consulta de egresados con validación de documento, certificación, contacto, ficha, fechas y autorización de datos.
- Creación automática de la vinculación académica inicial.
- Visor de Bienestar limitado a indicadores agregados; las rutas nominales se restringen a los perfiles autorizados.
- Catálogos de programas y fichas administrables desde Django Admin.

La certificación se registra contra una referencia que debe verificar el funcionario en el acta o sistema institucional; no existe integración con Sofía Plus. Las plantillas y operaciones de encuesta, empleo, reportes, alertas automáticas y auditoría funcional aún requieren implementación.

## Pruebas

```powershell
python manage.py test app_egresados
```