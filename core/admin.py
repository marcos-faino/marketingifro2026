from django.contrib import admin
from django.template.defaultfilters import truncatewords

from .models import Servico, Colaborador


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'get_bio')

    def get_bio(self, obj):
        return truncatewords(obj.bio, 12)

    get_bio.short_description = 'biografia'
