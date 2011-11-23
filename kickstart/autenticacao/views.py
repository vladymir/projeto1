#coding: utf-8

# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from autenticacao.forms import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template.loader import *
from django.contrib.auth import logout, authenticate, login
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from kickstart.autenticacao.forms import LoginForm, PropostaForm, RegistroForm
from kickstart.autenticacao.models import Proposta, Inbox, Perfil, Endereco
import datetime
from kickstart import autenticacao

def inicio(request):
    qnt_propst_listadas = 6
    propostas = Proposta.objects.all()
    ultimas_propostas = propostas.order_by('data_envio')[:qnt_propst_listadas].reverse()
    variables = Context({'user': request.user, 'propostas' : ultimas_propostas})
    return render_to_response('inicio.html', variables)

@login_required
def pagina_mensagem(request):
    user = request.user
    inbox = Inbox.objects.get(usuario_criador=user)
    mensagens = inbox.mensagem_set.all()
    variables = Context({'user': user, 'mensagens': mensagens})
    return render_to_response('mensagens.html', variables)
    
@login_required
def pagina_ver_mensagem(request, identificador):
    try:
        ident = int(identificador)
    except:
        raise Http404()
    user = request.user
    inbox = user.inbox_set.get(usuario_criador=user)
    mensagem = inbox.mensagem_set.get(id=ident)
    variables = Context({'user': user, 'mensagem' : mensagem})
    return render_to_response('ver_mensagem.html', variables)
    
def pagina_ver_proposta(request, identificador):
    try:
        ident = int(identificador)
    except:
        raise Http404()
    
    user = request.user
    if request.method == 'POST':
        form = autenticacao.forms.DoarForm(request.POST)
        if form.is_valid():
            proposta = Proposta.objects.get(id=ident)
            proposta.aumentar_arrecadado(form.cleaned_data['valor'])
            proposta.save()
            return HttpResponseRedirect('/sucesso')
        return HttpResponseRedirect('/')
    else:
        form = autenticacao.forms.DoarForm()
        proposta = Proposta.objects.get(id=ident)
        variables = RequestContext(request, 
                                   {'user': user, 'proposta' : proposta,
                                     'form' : form})
        return render_to_response('ver_proposta.html', variables)
    
def pagina_perfil(request):
    if request.user.is_authenticated():
        user = request.user
        perfil = user.get_profile()
        propostas = user.proposta_set.all()
        variables = Context({ 'perfil' : perfil, 'user': user , 'propostas':propostas })
        return render_to_response('perfil.html', variables)
    else:
        return HttpResponseRedirect('/registrar/')
    
def pagina_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def pagina_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                                username=form.cleaned_data['nome_usuario'],
                                password=form.cleaned_data['senha']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
        return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        variables = RequestContext(request, { 'form': form })
        return render_to_response('login.html', variables)
        
def pagina_proposta(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            propostaform = PropostaForm(request.POST)
            if propostaform.is_valid():
                novaProposta = propostaform.save(commit=False)
                novaProposta.usuario_criador = request.user
                novaProposta.status = 'P'
                novaProposta.data_envio = datetime.date.today()
                novaProposta.save()
                return HttpResponseRedirect('/sucesso')
            return HttpResponseRedirect('/')
            #return HttpResponse('Proposta Submetida com sucesso.')
        else:
            form = PropostaForm()
            variables = RequestContext(request, { 'form': form })
            return render_to_response('proposta.html', variables)
    else:
        return HttpResponseRedirect('/registrar/')

def pagina_registrar(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                        username=form.cleaned_data['nome_usuario'],
                        password=form.cleaned_data['senha1'],
                        email=form.cleaned_data['email'],
                        )
                
                endereco = Endereco()
                endereco.rua = form.cleaned_data['rua']
                endereco.numero = form.cleaned_data['numero']
                endereco.complemento = form.cleaned_data['complemento']
                endereco.cidade = form.cleaned_data['cidade']
                endereco.estado = form.cleaned_data['estado']
                endereco.save()
                
                perfil = Perfil()
                perfil.nome = form.cleaned_data['nome']
                perfil.sobrenome = form.cleaned_data['sobrenome']
                perfil.nascimento = form.cleaned_data['nascimento']
                perfil.telefone = form.cleaned_data['telefone']
                perfil.endereco = endereco
                perfil.user = user
                perfil.save()

                inbox = Inbox()
                inbox.usuario_criador = user
                inbox.save()
                user = authenticate(
                        username=form.cleaned_data['nome_usuario'], 
                        password=form.cleaned_data['senha1']
                        )
                if user is not None:
                    if user.is_active:
                        login(request, user)
                return HttpResponseRedirect('/sucesso')
            return HttpResponseRedirect('/')                    
        else:
            form = RegistroForm()
            variables = RequestContext(request, { 'form': form })
            return render_to_response('registrar.html', variables)
    else:
        return HttpResponseRedirect('/')
    
def ajuda(request):
    variables = Context({'user': request.user})
    return render_to_response('ajuda.html', variables)

def sucesso(request):
    variables = Context({'user': request.user})
    return render_to_response('sucesso.html', variables)

def categorias(request):
    categorias = ['Outra', 'Música', 'Desenho', 'Dança', 'Vídeo', 'Fotografia',
                  'Outras Artes', 'Tecnologia', 'Escrita', 'Jogos', 'Comida',
                  'Moda']
    variables = Context({'categorias' : categorias, 'user': request.user})
    return render_to_response('categorias.html', variables)
    
def ver_categoria(request, categoria):
    propostas = Proposta.objects.filter(categoria=categoria)
    
    variables = Context({'categoria' : categoria, 'propostas' : propostas,
                          'user': request.user})
    return render_to_response('ver_categoria.html', variables)