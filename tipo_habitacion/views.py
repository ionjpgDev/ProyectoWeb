from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoHabitacion
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import TipoHabitacionForm
@staff_member_required
def lista_tipo_habitacion(request):
    tipos = TipoHabitacion.objects.all()
    form = TipoHabitacionForm()

    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tipo_habitacion')

    return render(request, 'tipo_habitacion/lista_tipo_habitacion.html', {
        'tipos': tipos,
        'form': form,
        'accion': 'Agregar',
        'editando': False
    })
@staff_member_required
def editar_tipo_habitacion(request, tipo_id):
    tipo = get_object_or_404(TipoHabitacion, id=tipo_id)
    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('lista_tipo_habitacion')
    else:
        form = TipoHabitacionForm(instance=tipo)

    tipos = TipoHabitacion.objects.all()
    return render(request, 'tipo_habitacion/lista_tipo_habitacion.html', {
        'tipos': tipos,
        'form': form,
        'accion': 'Editar',
        'editando': True
    })
@staff_member_required
def eliminar_tipo_habitacion(request, tipo_id):
    tipo = get_object_or_404(TipoHabitacion, id=tipo_id)
    tipo.delete()
    return redirect('lista_tipo_habitacion')
