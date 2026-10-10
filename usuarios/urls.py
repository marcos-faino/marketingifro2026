from django.urls import path

from usuarios.views import NovoUsuario

urlpatterns = [
    path('novo/', NovoUsuario.as_view(), name='novouser'),
]