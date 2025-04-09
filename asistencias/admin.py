from django.contrib import admin
from .models import Usuario, Plan, Asistencia

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre_plan', 'frecuencia', 'monto', 'fecha_inicio', 'fecha_termino', 'estado')
    list_filter = ('nombre_plan', 'frecuencia', 'estado')
    search_fields = ('usuario__nombre',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'plan', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('usuario__nombre',)
