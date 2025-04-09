from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),  # 👈 Esto redirige raíz al dashboard
   # path("usuarios/", include("usuarios.urls")),
  #  path("planes/", include("planes.urls")),
    path("asistencia/", include("asistencias.urls")),
]
