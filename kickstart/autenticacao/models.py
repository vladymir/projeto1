#coding: utf-8
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=20, default="", null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

class Perfil(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    nascimento = models.DateField()
    endereco = models.ForeignKey(Endereco)
    telefone = models.CharField(max_length=20)
    user = models.ForeignKey(User,
                              unique=True, related_name='%(class)s_user')

PROPOSTA_STATUS = (
    ('N', 'Negada'),
    ('A', 'Aceita'),
    ('P', 'Pendente'),
)
class Proposta(models.Model):
    usuario_criador = models.ForeignKey(User)
    titulo = models.CharField(max_length=60)
    o_que = models.CharField(max_length=700)
    recompensas = models.CharField(max_length=1000)
    mais_infos = models.CharField(max_length=700)
    categoria = models.CharField(max_length=50)
    quanto = models.IntegerField()
    contato = models.CharField(max_length=80)
    status = models.CharField(max_length=1, choices=PROPOSTA_STATUS)
    data_envio = models.DateTimeField("Data de publicação")

    def __unicode__(self):
        return self.titulo
    
    def get_resumo(self):
        return self.o_que[0:120]

class Projeto(models.Model):
    usuario_criador = models.ForeignKey(User)
    proposta = models.ForeignKey(Proposta)
    post = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.post

class Doacao(models.Model):
    usuario_doador = models.ForeignKey(User)
    projeto = models.ForeignKey(Projeto)
    valor = models.IntegerField()

    def __unicode__(self):
        return self.valor

class Comentario(models.Model):
    projeto = models.ForeignKey(Projeto)
    comentario = models.TextField()
    
class Inbox(models.Model):
    usuario_criador = models.ForeignKey(User)
    
    def __unicode__(self):
        return 'Caixa de Entrada'

class Mensagem(models.Model):
    inbox = models.ForeignKey(Inbox)
    remetente = models.ForeignKey(User)
    mensagem = models.TextField()

    def __unicode__(self):
        return self.remetente.email

# Create your models here.

@receiver(post_save, sender=Proposta)
def my_handler(sender, **kwargs):
    proposta = kwargs['instance']
    user = proposta.usuario_criador
    inbox = Inbox.objects.get(usuario_criador=user.id)
    if proposta.status=='A':
        mensagem = Mensagem.objects.create(inbox_id=inbox.id,remetente_id=1 ,
                                        mensagem='Sua proposta foi aceita!!')
        mensagem.save()
    elif proposta.status == 'N':
        mensagem = Mensagem.objects.create(inbox_id=inbox.id,remetente_id=1 ,
                                        mensagem='Sua proposta foi negada!!')
        mensagem.save()
