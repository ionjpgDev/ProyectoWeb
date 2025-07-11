

from django.urls import path
from . import views

urlpatterns = [

    path('editar/<int:cliente_id>/', views.lista_cliente, name='editar_cliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('lista_cliente/', views.lista_cliente, name='lista_cliente'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
]
