from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=250)
    mensagem = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']

        conteudo = (f'mensagem de : {nome}\n'
                    f'{mensagem}')
        mail = EmailMessage(
            subject = f'Contato do cliente {nome}',
            body = conteudo,
            from_email = 'marcosfaino@gmail.com',
            to = ['marcos.faino@ifro.edu.br'],
            headers = {'Reply-To': email},
        )
        mail.send()