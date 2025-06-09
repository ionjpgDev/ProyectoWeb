from django.urls import path
from . import views
urlpatterns = [
    path('lista_tipo_habitacion/', views.lista_tipo_habitacion, name='lista_tipo_habitacion'),
    path('editar_tipo_habitacion/<int:tipo_id>/', views.editar_tipo_habitacion, name='editar_tipo_habitacion'),
    path('eliminar_tipo_habitacion/<int:tipo_id>/', views.eliminar_tipo_habitacion, name='eliminar_tipo_habitacion'),
]
