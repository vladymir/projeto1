#coding: utf-8

from django import forms
from django.forms.widgets import RadioSelect
from kickstart.autenticacao.models import Proposta

class RegistroForm(forms.Form):
    FORMATO_DATA_ACEITO = ('%d/%m/%Y', '%d/%m/%y',
                           '%d %b %Y', '%d %b, %Y',)
    
    nome_usuario = forms.CharField(label=u'Nome de Usuário', max_length=30)
    senha1 = forms.CharField(
                             label=u'Senha',
                             widget=forms.PasswordInput()
                             )

    senha2 = forms.CharField(
                             label=u'Senha (confirmacao)',
                             widget=forms.PasswordInput()
                             )
    email = forms.EmailField(label=u'Email')
    nascimento = forms.DateField(
                                 label=u'Data de Nascimento',
                                 input_formats=FORMATO_DATA_ACEITO
                                 )
    nome = forms.CharField(max_length=20)
    sobrenome = forms.CharField(max_length=20)
    telefone = forms.CharField(label=u'Telefone para Contato', max_length=20)
    rua = forms.CharField(label=u'Rua', max_length=100)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length=20, required=False)
    cidade = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=2)
    
class DoarForm(forms.Form):
    ESCOLHA_VALOR = ((1, 'R$ 1,00'), (5, 'R$ 5,00'), (10, 'R$ 10,00'),
                     (25, 'R$ 25,00'), (50, 'R$ 50,00'), (100, 'R$ 100,00'))
    valor = forms.ChoiceField(widget=RadioSelect, choices=ESCOLHA_VALOR)
    
    

class LoginForm(forms.Form):
    nome_usuario = forms.CharField(label=u'Nome do usuario', max_length=30)
    senha = forms.CharField(label=u'Senha',
                            widget=forms.PasswordInput())
   
class PropostaForm(forms.ModelForm):
    ESCOLHA_CATEGORIA = (('Outra', 'Outra'), ('Música', 'Música'),
                         ('Desenho', 'Desenho'), ('Dança', 'Dança'),
                         ('Vídeo', 'Vídeo'), ('Fotografia', 'Fotografia'),
                         ('Outras Artes', 'Outras Artes'), ('Tecnologia', 'Tecnologia'),
                         ('Escrita', 'Escrita'), ('Jogos', 'Jogos'),
                         ('Comida', 'Comida'), ('Moda', 'Moda')) 
    
    o_que = forms.CharField(
                            label="Descrição do projeto",
                            widget=forms.Textarea({'rows':10, 'cols': 70, })
                            )
    recompensas = forms.CharField(widget=forms.Textarea({'rows':12, 'cols': 70, }))
    mais_infos = forms.CharField(
                                 label="Mais Informações",
                                 widget=forms.Textarea({'rows':8, 'cols': 70, })
                                 )
    categoria = forms.ChoiceField(
                                  widget=forms.Select,
                                  choices=ESCOLHA_CATEGORIA
                                  )
    quanto = forms.IntegerField(label="Capital Necessário")
    
    class Meta:
        model = Proposta
        exclude = ('status', 'usuario_criador', 'data_envio', 'arrecadado', 'percentual')
