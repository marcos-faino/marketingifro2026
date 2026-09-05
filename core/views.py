from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from core.models import Servico, Colaborador
from core.forms import ContatoForm


class HomeView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('home')

    # adicionando dados ao contexto do template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by("?").all()
        context['colaboradores'] = Colaborador.objects.order_by("?").filter(ativo=True)
        return context

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o email!')
        return super().form_invalid(form)


class ServicoDetailView(DetailView):
    model = Servico
    template_name = 'detalhe/servico.html'
    context_object_name = 'servico'