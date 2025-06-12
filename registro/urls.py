from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('accounts/logout/', LogoutView.as_view(next_page='/', http_method_names=['post']), name='logout'),
    path('accounts/login/', LoginView.as_view(template_name='registro/login.html'), name='login'),
]