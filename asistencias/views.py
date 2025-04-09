from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Plan, Asistencia, Usuario
from .forms import RegistrarAsistenciaForm
from django.contrib import messages
from .forms import UsuarioForm, PlanForm
from django.db import IntegrityError

def registrar_asistencia(request):
    if request.method == "POST":
        form = RegistrarAsistenciaForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            hoy = timezone.now().date()

            # Verificar si ya tiene asistencia hoy
            if Asistencia.objects.filter(usuario=usuario, fecha=hoy).exists():
                messages.warning(request, f"{usuario.nombre} ya registró asistencia hoy.")
                return redirect("registrar_asistencia")

            plan = Plan.objects.filter(
                usuario=usuario,
                estado="activo",
                fecha_inicio__lte=hoy,
                fecha_termino__gte=hoy
            ).order_by("-fecha_inicio").first()

            if not plan:
                messages.error(request, f"{usuario.nombre} no tiene un plan activo.")
                return redirect("registrar_asistencia")

            if plan.dias_disponibles <= 0:
                messages.error(request, f"{usuario.nombre} no tiene días disponibles en su plan.")
                return redirect("registrar_asistencia")

            try:
                Asistencia.objects.create(usuario=usuario, plan=plan)
                plan.dias_disponibles -= 1
                plan.save()
                messages.success(request, f"Asistencia registrada para {usuario.nombre}. ¡Quedan {plan.dias_disponibles} días!")
            except IntegrityError:
                messages.warning(request, f"{usuario.nombre} ya tiene una asistencia registrada hoy (control de base de datos).")

            return redirect("registrar_asistencia")
    else:
        form = RegistrarAsistenciaForm()

    return render(request, "asistencias/registrar_asistencia.html", {"form": form})

# ✅ Usuario
def registrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Usuario registrado con éxito")
            return redirect("dashboard")
    else:
        form = UsuarioForm()

    return render(request, "formulario.html", {
        "form": form,
        "titulo": "Registrar Usuario",
        "boton": "Registrar"
    })

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Usuario actualizado correctamente")
            return redirect("listar_usuarios")
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, "formulario.html", {
        "form": form,
        "titulo": "Editar Usuario",
        "boton": "Guardar Cambios"
    })

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request, "🗑️ Usuario eliminado correctamente.")
    return redirect("listar_usuarios")

# ✅ Plan
def registrar_plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Plan registrado con éxito")
            return redirect("listar_planes")
    else:
        form = PlanForm()

    return render(request, "formulario.html", {
        "form": form,
        "titulo": "Registrar Plan",
        "boton": "Registrar"
    })

def editar_plan(request, id):
    plan = get_object_or_404(Plan, id=id)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Plan actualizado correctamente")
            return redirect("listar_planes")
    else:
        form = PlanForm(instance=plan)

    return render(request, "formulario.html", {
        "form": form,
        "titulo": "Editar Plan",
        "boton": "Guardar Cambios"
    })

def eliminar_plan(request, id):
    plan = Plan.objects.get(id=id)
    plan.delete()
    messages.success(request, "🗑️ Plan eliminado correctamente.")
    return redirect("listar_planes")

# ✅ Listados
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "asistencias/listar_usuarios.html", {"usuarios": usuarios})

def listar_planes(request):
    planes = Plan.objects.select_related("usuario").all()
    return render(request, "asistencias/listar_planes.html", {"planes": planes})