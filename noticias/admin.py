from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','nomeautor','status','criado_em')
    fields = ('titulo','slug', 'texto','status','imagem_principal')
    prepopulated_fields = {'slug':('titulo',)}
    list_editable = ('status',)
    list_filter = ('status','autor')

    def nomeautor(self,obj):
        return obj.autor.get_full_name()

    nomeautor.short_description = 'autor'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)