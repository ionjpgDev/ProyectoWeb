from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

@staff_member_required
def lista_cliente(request, cliente_id=None):
    if cliente_id:
        cliente = get_object_or_404(Cliente, id=cliente_id)
        form = ClienteForm(request.POST or None, instance=cliente)
        accion = 'Editar'
    else:
        form = ClienteForm(request.POST or None)
        accion = 'Crear'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_cliente')

    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_cliente.html', {
        'clientes': clientes,
        'form': form,
        'accion': accion,
        'editando': cliente_id is not None
    })

@staff_member_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_cliente')
