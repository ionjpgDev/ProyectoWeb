from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from 

def index(request):
    return render(request,'index.html')

def lista_reserva(request):
    reservas = Reserva.objects.all()
    form = ReservaForm()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reserva')

    return render(request, 'reserva/lista_reserva.html', {
        'reservas': reservas,
        'form': form,
        'accion': 'Agregar',
        'editando': False
    })

def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reserva')
    else:
        form = ReservaForm(instance=reserva)

    reservas = Reserva.objects.all()
    return render(request, 'reserva/lista_reserva.html', {
        'reservas': reservas,
        'form': form,
        'accion': 'Editar',
        'editando': True
    })

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('lista_reserva')
