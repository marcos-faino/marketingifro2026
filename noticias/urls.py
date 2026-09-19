from django.urls import path
from noticias import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ListaNoticias.as_view(), name='noticias'),
]