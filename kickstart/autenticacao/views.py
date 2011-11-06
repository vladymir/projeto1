# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from autenticacao.forms import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template.loader import *
from django.contrib.auth import logout, authenticate, login
from autenticacao.models import Proposta, Usuario
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

def inicio(request):
    variables = Context({'user': request.user})
    return render_to_response('inicio.html', variables)

@login_required
def pagina_ver_proposta(request, identificador):
    try:
        ident = int(identificador)
    except:
        raise Http404()
    
    user = request.user
    proposta = user.proposta_set.get(id=ident)
    variables = Context({'user': user, 'proposta' : proposta})
    return render_to_response('ver_proposta.html', variables)
    
def pagina_perfil(request):
    if request.user.is_authenticated():
        user = request.user
        propostas = user.proposta_set.all()
        variables = Context({ 'user': user , 'propostas':propostas })
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
                novaProposta.save()
            return HttpResponseRedirect('/inicio/')
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
                        email=form.cleaned_data['email']
                        )
                user = authenticate(
                        username=form.cleaned_data['nome_usuario'], 
                        password=form.cleaned_data['senha1']
                        )
                if user is not None:
                    if user.is_active:
                        login(request, user)

                return HttpResponseRedirect('/')
            #return HttpResponse(user.username + 'Registrado Com Sucesso')
                    
        else:
            form = RegistroForm()
            variables = RequestContext(request, { 'form': form })
            return render_to_response('registrar.html', variables)
    else:
        return HttpResponseRedirect('/')
    
def ajuda(request):
    return render_to_response('ajuda.html')