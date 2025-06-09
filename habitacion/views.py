# habitacion/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habitacion
from .forms import HabitacionForm

def index(request):
    habitaciones = Habitacion.objects.all()
    form = HabitacionForm()

    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_habitacion')  # nombre de tu url para esta vista

    return render(request, 'habitacion/lista_habitacion.html', {
        'habitaciones': habitaciones,
        'form': form,
        'accion': 'Agregar',
        'editando': False
    })

def editar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('lista_habitacion')
    else:
        form = HabitacionForm(instance=habitacion)

    habitaciones = Habitacion.objects.all()
    return render(request, 'habitacion/lista_habitacion.html', {
        'habitaciones': habitaciones,
        'form': form,
        'accion': 'Editar',
        'editando': True
    })

def eliminar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    habitacion.delete()
    return redirect('lista_habitacion')
