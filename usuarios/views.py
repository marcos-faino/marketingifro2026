from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView


from usuarios.forms import CadUsuarioForm


class NovoUsuario(CreateView):
    template_name = 'usuarios/novo.html'
    form_class = CadUsuarioForm
    success_url = reverse_lazy('loginuser')

    def form_valid(self, form):
        form.cleaned_data
        grupo = get_object_or_404(Group, name='colaboradores')
        user = form.save()
        user.groups.add(grupo)
        messages.success(self.request, 'Usuario cadastrado com sucesso')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar')
        return super().form_invalid(form)
