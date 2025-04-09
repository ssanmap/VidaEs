from django import forms
from .models import Usuario
from .models import Plan


class RegistrarAsistenciaForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), label="Selecciona al usuario")


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [
            'usuario', 'nombre_plan', 'frecuencia', 'monto',
            'metodo_pago', 'fecha_inicio', 'fecha_termino',
            'dias_disponibles', 'estado'
        ]
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'nombre_plan': forms.Select(attrs={'class': 'form-control'}),
            'frecuencia': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'metodo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'dias_disponibles': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }
