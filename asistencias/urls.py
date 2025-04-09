from django.urls import path
from .views import registrar_asistencia
from . import views


urlpatterns = [
    path('registrar/', registrar_asistencia, name="registrar_asistencia"),
    path("registrar-usuario/", views.registrar_usuario, name="registrar_usuario"),
    path("registrar-plan/", views.registrar_plan, name="registrar_plan"),
    path("usuarios/", views.listar_usuarios, name="listar_usuarios"),
    path("planes/", views.listar_planes, name="listar_planes"),
     # ✅ Agregar estas rutas
    path("editar-usuario/<int:id>/", views.editar_usuario, name="editar_usuario"),
    path("eliminar-usuario/<int:id>/", views.eliminar_usuario, name="eliminar_usuario"),
     
]
