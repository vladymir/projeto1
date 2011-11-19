#coding: utf-8

from django import forms
from django.forms.fields import ChoiceField
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
    ESCOLHA_CATEGORIA = (('Outra', 'Outra'), ('Música','Música'),
                         ('Desenho', 'Desenho'),('Dança', 'Dança'),
                         ('Vídeo', 'Vídeo'), ('Fotografia','Fotografia'),
                         ('Outras Artes', 'Outras Artes'), ('Tecnologia','Tecnologia'),
                         ('Escrita', 'Escrita'), ('Jogos', 'Jogos'),
                         ('Comida', 'Comida'), ('Moda', 'Moda')) 
    
    o_que = forms.CharField(label="Descrição do projeto", widget=forms.Textarea({'rows':10, 'cols': 70,}))
    recompensas = forms.CharField( widget=forms.Textarea({'rows':12, 'cols': 70,}))
    mais_infos = forms.CharField(label="Mais Informações", widget=forms.Textarea({'rows':8, 'cols': 70,}))
    categoria = forms.ChoiceField(widget=forms.Select, choices=ESCOLHA_CATEGORIA)
    quanto = forms.IntegerField(label="Capital Necessário")
    
    class Meta:
        model = Proposta
        exclude = ('status','usuario_criador','data_envio',)