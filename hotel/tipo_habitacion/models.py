from django.db import models

class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    capacidad = models.PositiveIntegerField()
    servicios = models.TextField(help_text="Lista de servicios separados por comas")

    def __str__(self):
        return self.nombre