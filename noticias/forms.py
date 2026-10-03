from django.core.mail.message import EmailMessage

from django import forms


class NoticiaForm(forms.Form):
    nome = forms.CharField(widget=forms.HiddenInput())
    titulo = forms.CharField(widget=forms.HiddenInput)
    resumo = forms.CharField(widget=forms.HiddenInput)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        urlnew = self.cleaned_data['titulo']
        resnew = self.cleaned_data['resumo']
        mensagem = (f'Olá! Dá uma olhada nesta notícia:\n'
                    f'{urlnew}\n'
                    f'{resnew}\n')

        mail = EmailMessage(
            subject = f'Compartilhamento de notícia',
            body = mensagem,
            from_email = 'marcosfaino@gmail.com',
            to = ['marcos.faino@ifro.edu.br'],
            headers = {'Reply-To': 'marcosfaino@gmail.com'},
        )
        mail.send()