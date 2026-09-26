from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','nomeautor','status','criado_em')
    fields = ['titulo','slug', 'texto','imagem_principal']
    campo_oculto = ['status']
    prepopulated_fields = {'slug':('titulo',)}
    # list_editable = ('status',)
    list_filter = ('autor',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.fields + self.campo_oculto
        return self.fields

    def get_list_display(self, request):
        if request.user.is_superuser:
            self.list_editable = ('status',)
        else:
            self.list_editable = []
        return self.list_display

    def nomeautor(self,obj):
        return obj.autor.get_full_name()

    nomeautor.short_description = 'autor'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            return super().save_model(request, obj, form, change)
        obj.autor = request.user
        return super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return super().has_delete_permission(request, obj)
        # Outros usuários só poderão excluir e alterar se a notícia
        # não estiver sido publicada.
        elif obj and not request.user.is_superuser and obj.status == 'rascunho':
            return super().has_delete_permission(request, obj)
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user.is_superuser:
            return super().has_change_permission(request, obj)
        # Outros usuários só poderão alterar se a notícia
        # não estiver sido publicada.
        elif obj and not request.user.is_superuser and obj.status == 'rascunho':
            return super().has_change_permission(request, obj)
        return False

