from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Servico(Base):
    imagem = StdImageField(upload_to='servicos',
                           variations={'thumb': {'width': 471,
                                                 'height': 216,
                                                 'crop': True}})
    icone = models.CharField(max_length=80)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome


class Colaborador(Base):
    CARGOS = {
        'coordenador': 'Coordenador',
        'jornalista': 'Jornalista',
        'fotografo': 'Fotógrafo(a)',
        'designer': 'Designer',
    }
    foto = StdImageField(upload_to='colaboradores',)
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=11, choices=CARGOS)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome


class Campus(Base):
    nome = models.CharField(max_length=200)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE,
                                  related_name='campus')

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campi'

    def __str__(self):
        return self.nome

class Municipio(Base):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    def __str__(self):
        return self.nome