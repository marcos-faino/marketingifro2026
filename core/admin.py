from django.contrib import admin
from django.template.defaultfilters import truncatewords

from .models import Servico, Colaborador, Municipio, Campus


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_endereco', 'municipio')

    def get_endereco(self, obj):
        return f'Rua:{obj.rua}, {obj.numero}. Bairro {obj.bairro}'

    get_endereco.short_description = 'endereço'


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'get_bio')

    def get_bio(self, obj):
        return truncatewords(obj.bio, 12)

    get_bio.short_description = 'biografia'
