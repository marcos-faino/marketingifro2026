from django.views.generic import ListView

from noticias.models import Noticia


class ListaNoticias(ListView):
    template_name = 'new/listar.html'
    model = Noticia
    queryset = Noticia.publicados.all()
    context_object_name = 'noticias'
    paginate_by = 3
