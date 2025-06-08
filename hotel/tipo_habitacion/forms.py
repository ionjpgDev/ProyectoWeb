from django import forms
from .models import TipoHabitacion

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = ['nombre', 'descripcion', 'precio', 'capacidad', 'servicios']
