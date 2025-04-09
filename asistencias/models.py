from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Plan(models.Model):
    TIPO_PLAN = [
        ("nuevo", "Nuevo ingreso"),
        ("pareja", "Plan pareja"),
        ("convenio", "Convenio empresa"),
        ("normal", "Plan normal"),
    ]

    FRECUENCIA = [
        ("3xsemana", "3 veces por semana"),
        ("todos", "Todos los días"),
        ("2xsemana", "2 veces por semana"),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_plan = models.CharField(max_length=50, choices=TIPO_PLAN)
    frecuencia = models.CharField(max_length=20, choices=FRECUENCIA)
    monto = models.PositiveIntegerField(help_text="Monto en CLP")
    metodo_pago = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_termino = models.DateField()
    dias_disponibles = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, default="activo")

    def __str__(self):
        return f"{self.usuario.nombre} - {self.get_nombre_plan_display()}"


class Asistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'fecha')

    def __str__(self):
        return f"{self.usuario.nombre} - {self.fecha}"
