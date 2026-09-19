from django.contrib.auth import get_user_model
from django.db import models
from stdimage import StdImageField


class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publicado')


class Noticia(models.Model):
    objects = models.Manager()
    publicados = PublicadosManager()

    STATUS_CHOICES = (
        ('publicado', 'Publicado'),
        ('rascunho', 'Rascunho'),
    )
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES,
                              default='rascunho')
    autor = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1)
    imagem_principal = StdImageField(upload_to='servicos',
                                    variations={'thumb': {'width': 480,
                                                 'height': 360,
                                                 'crop': True}})


    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['status', '-criado_em']

    def __str__(self):
        return self.titulo