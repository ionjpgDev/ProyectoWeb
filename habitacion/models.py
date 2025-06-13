from django.db import models
from tipo_habitacion.models import TipoHabitacion

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    piso = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo.nombre}'