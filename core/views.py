from django.views.generic import TemplateView

from core.models import Servico, Colaborador


class HomeView(TemplateView):
    template_name = 'index.html'

    # adicionando dados ao contexto do template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by("?").all()
        context['colaboradores'] = Colaborador.objects.order_by("?").all()
        return context
