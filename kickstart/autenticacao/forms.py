#coding: utf-8

from django import forms
from kickstart.autenticacao.models import Proposta

class RegistroForm(forms.Form):
    nome_usuario = forms.CharField(label=u'Nome de Usuario', max_length=30)
    email = forms.EmailField(label=u'Email')
    senha1 = forms.CharField(
            label=u'Senha',
            widget=forms.PasswordInput()
    )

    senha2 = forms.CharField(
            label=u'Senha (confirmacao)',
            widget=forms.PasswordInput()
    )

class LoginForm(forms.Form):
    nome_usuario = forms.CharField(label=u'Nome do usuario', max_length=30)
    senha = forms.CharField(label=u'Senha',
                            widget=forms.PasswordInput()
                            )
class PropostaForm(forms.ModelForm):
    como_descobriu = forms.CharField(max_length=100, required=False)
    class Meta:
        model = Proposta
        exclude = ('status','usuario_criador','data_envio',)