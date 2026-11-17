"""Vistas MVT para el panel y la gestión operativa de egresados."""

from functools import wraps

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import EgresadoForm
from .models import AccionSeguimiento, Egresado, Programa


def rol_requerido(*roles):
    """Restringe una vista a superusuarios o miembros de grupos autorizados."""

    def decorador(vista):
        """Envuelve la vista con la validación del grupo del usuario."""

        @wraps(vista)
        @login_required
        def protegida(request, *args, **kwargs):
            """Comprueba el rol y devuelve una respuesta de acceso denegado."""

            if request.user.is_superuser or request.user.groups.filter(
                name__in=roles
            ).exists():
                return vista(request, *args, **kwargs)
            return render(request, 'app_egresados/forbidden.html', status=403)

        return protegida

    return decorador


def contexto_navegacion(usuario):
    """Calcula capacidades de navegación sin exponer grupos en plantillas."""

    roles = set(usuario.groups.values_list('name', flat=True))
    administrador = usuario.is_superuser or 'Administrador' in roles
    funcionario = 'Funcionario' in roles
    coordinador = 'Visor - Coordinador Académico' in roles
    bienestar = 'Visor - Bienestar al Aprendiz' in roles
    return {
        'acceso_nominal': administrador or funcionario or coordinador,
        'puede_gestionar_egresados': administrador or funcionario,
        'es_bienestar': bienestar,
    }


def iniciar_sesion_view(request):
    """Autentica a usuarios institucionales mediante el sistema Django."""

    if request.user.is_authenticated:
        return redirect('inicio')
    formulario = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        login(request, formulario.get_user())
        return redirect('inicio')
    return render(
        request,
        'app_egresados/login.html',
        {'formulario': formulario},
    )


@login_required
@require_http_methods(['POST'])
def cerrar_sesion_view(request):
    """Cierra la sesión activa y redirige al formulario de acceso."""

    logout(request)
    return redirect('iniciar_sesion')


@rol_requerido(
    'Administrador', 'Funcionario', 'Visor - Coordinador Académico',
    'Visor - Bienestar al Aprendiz',
)
def inicio_view(request):
    """Muestra indicadores y registros recientes del centro."""

    egresados = Egresado.objects.select_related('programa', 'ficha')
    contexto = {
        'total_egresados': egresados.count(),
        'validados': egresados.filter(
            estado__in=[Egresado.Estado.VALIDADO, Egresado.Estado.SEGUIMIENTO]
        ).count(),
        'pendientes': egresados.filter(
            estado=Egresado.Estado.PENDIENTE
        ).count(),
        'desactualizados': egresados.filter(
            estado=Egresado.Estado.DESACTUALIZADO
        ).count(),
        'programas_activos': Programa.objects.filter(activo=True).count(),
        'ultimos_egresados': egresados[:6],
        'alertas': egresados.filter(
            estado__in=[
                Egresado.Estado.PENDIENTE,
                Egresado.Estado.DESACTUALIZADO,
                Egresado.Estado.NO_LOCALIZABLE,
            ]
        )[:5],
    }
    contexto.update(contexto_navegacion(request.user))
    if contexto['es_bienestar']:
        contexto['ultimos_egresados'] = []
        contexto['alertas'] = []
    return render(request, 'app_egresados/dashboard.html', contexto)


@rol_requerido(
    'Administrador', 'Funcionario', 'Visor - Coordinador Académico'
)
def egresados_list_view(request):
    """Busca y filtra egresados según texto, estado y programa."""

    egresados = Egresado.objects.select_related('programa', 'ficha')
    consulta = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')
    programa_id = request.GET.get('programa', '')
    if consulta:
        egresados = egresados.filter(
            Q(nombres__icontains=consulta)
            | Q(apellidos__icontains=consulta)
            | Q(documento__icontains=consulta)
            | Q(programa__nombre__icontains=consulta)
        )
    if estado in Egresado.Estado.values:
        egresados = egresados.filter(estado=estado)
    if programa_id.isdigit():
        egresados = egresados.filter(programa_id=programa_id)
    contexto = {
        'egresados': egresados,
        'programas': Programa.objects.filter(activo=True),
        'estados': Egresado.Estado.choices,
        'consulta': consulta,
        'estado_seleccionado': estado,
        'programa_seleccionado': programa_id,
    }
    contexto.update(contexto_navegacion(request.user))
    return render(
        request,
        'app_egresados/egresados_list.html',
        contexto,
    )


@rol_requerido('Administrador', 'Funcionario')
@require_http_methods(['GET', 'POST'])
def egresados_create_view(request):
    """Crea un egresado tras validar certificación y reglas de negocio."""

    formulario = EgresadoForm(request.POST or None)
    if request.method == 'POST' and formulario.is_valid():
        egresado = formulario.save()
        messages.success(request, 'El egresado quedó registrado correctamente.')
        return redirect('egresado_detalle', pk=egresado.pk)
    return render(
        request,
        'app_egresados/egresado_form.html',
        {
            'formulario': formulario,
            **contexto_navegacion(request.user),
        },
    )


@rol_requerido(
    'Administrador', 'Funcionario', 'Visor - Coordinador Académico'
)
def egresados_detail_view(request, pk):
    """Presenta el detalle de un egresado y sus acciones de seguimiento."""

    egresado = get_object_or_404(
        Egresado.objects.select_related('programa', 'ficha'),
        pk=pk,
    )
    acciones = AccionSeguimiento.objects.filter(
        egresado=egresado
    ).select_related('funcionario')
    return render(
        request,
        'app_egresados/egresado_detail.html',
        {
            'egresado': egresado,
            'acciones': acciones,
            **contexto_navegacion(request.user),
        },
    )