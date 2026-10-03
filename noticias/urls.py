from django.urls import path
from noticias import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ListaNoticias.as_view(), name='noticias'),
    path('noticia/<int:pk>', views.DetailNoticia.as_view(), name='detalhe_noticia'),
    path('noticia/enviar', views.EnviarNoticia.as_view(), name='enviarnew'),
    path('comentario/noticia/<int:idnoticia>', views.Comentario.as_view(),
         name='coment'),
]