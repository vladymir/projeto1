#coding: utf-8

from django.conf.urls.defaults import patterns, include, url
from kickstart.autenticacao import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning.views.home', name='home'),
    # url(r'^learning/', include('learning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio),
    url(r'^registrar/$', views.pagina_registrar),
    url(r'^inicio/$', views.inicio),
    url(r'^logout/$', views.pagina_logout),
    url(r'^login/$', views.pagina_login),
    url(r'^perfil/$', views.pagina_perfil),
    url(r'^proposta/new/$', views.pagina_proposta),
    url(r'^propostas/(\d+)/$', views.pagina_ver_proposta),
    url(r'^ajuda/', views.ajuda),
    url(r'^sucesso/', views.sucesso),
    url(r'^mensagem/(\d+)/$', views.pagina_ver_mensagem),
    url(r'^mensagens/$', views.pagina_mensagem),
    url(r'^categorias/$', views.categorias),
    url(r'^categorias/(\w+)/', views.ver_categoria)
)