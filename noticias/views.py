from email.message import EmailMessage

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from noticias.forms import NoticiaForm, ComentarioForm
from noticias.models import Noticia, Comentario


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


class Comentario(FormView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/novo.html'
    context_object_name = 'comentario'
    noticia = None

    def form_valid(self, form):
        coment = form.save(commit=False)
        coment.autor = self.request.user
        self.noticia = Noticia.objects.get(id=self.kwargs['idnoticia'])
        coment.noticia = self.noticia
        coment.save()
        return redirect('noticias:detalhe_noticia', idnoticia)

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont['noticia'] = self.noticia
        return cont

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)