from django.urls import path
from . import views
urlpatterns = [
    path('lista_habitacion/', views.index, name='lista_habitacion'), 
    path('editar_habitacion/<int:habitacion_id>/', views.editar_habitacion, name='editar_habitacion'),
    path('eliminar_habitacion/<int:habitacion_id>/', views.eliminar_habitacion, name='eliminar_habitacion'),
]
