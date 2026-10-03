from email.message import EmailMessage

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from noticias.forms import NoticiaForm
from noticias.models import Noticia


class ListaNoticias(ListView):
    template_name = 'new/listar.html'
    model = Noticia
    queryset = Noticia.publicados.all()
    context_object_name = 'noticias'
    paginate_by = 3

class DetailNoticia(DetailView):
    template_name = 'new/detalhe.html'
    model = Noticia
    context_object_name = 'noticia'


class EnviarNoticia(FormView):
    form_class = NoticiaForm
    template_name = ('new/detalhe.html')
    success_url = reverse_lazy('noticias:noticias')

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o email!')
        return super().form_invalid(form)
