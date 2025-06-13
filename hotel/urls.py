from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from reserva.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls')),
    path('', include('habitacion.urls')),
    path('', include('reserva.urls')),
    path('', include('tipo_habitacion.urls')),
    path('', include('registro.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'), 
]

handler404 = 'reserva.views.custom_404_view'
