# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Usuario'
        db.create_table('autenticacao_usuario', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('autenticacao', ['Usuario'])

        # Adding model 'Endereco'
        db.create_table('autenticacao_endereco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rua', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('autenticacao', ['Endereco'])

        # Adding model 'Perfil'
        db.create_table('autenticacao_perfil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nascimento', self.gf('django.db.models.fields.DateField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sobrenome', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Endereco'])),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('autenticacao', ['Perfil'])

        # Adding model 'Proposta'
        db.create_table('autenticacao_proposta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario_criador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('o_que', self.gf('django.db.models.fields.CharField')(max_length=700)),
            ('recompensas', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('mais_infos', self.gf('django.db.models.fields.CharField')(max_length=700)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('quanto', self.gf('django.db.models.fields.IntegerField')()),
            ('como_descobriu', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('data_envio', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('autenticacao', ['Proposta'])

        # Adding model 'Projeto'
        db.create_table('autenticacao_projeto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario_criador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Usuario'])),
            ('proposta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Proposta'])),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('autenticacao', ['Projeto'])

        # Adding model 'Doacao'
        db.create_table('autenticacao_doacao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario_doador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Usuario'])),
            ('projeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Projeto'])),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('autenticacao', ['Doacao'])

        # Adding model 'Comentario'
        db.create_table('autenticacao_comentario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Projeto'])),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('autenticacao', ['Comentario'])


    def backwards(self, orm):
        
        # Deleting model 'Usuario'
        db.delete_table('autenticacao_usuario')

        # Deleting model 'Endereco'
        db.delete_table('autenticacao_endereco')

        # Deleting model 'Perfil'
        db.delete_table('autenticacao_perfil')

        # Deleting model 'Proposta'
        db.delete_table('autenticacao_proposta')

        # Deleting model 'Projeto'
        db.delete_table('autenticacao_projeto')

        # Deleting model 'Doacao'
        db.delete_table('autenticacao_doacao')

        # Deleting model 'Comentario'
        db.delete_table('autenticacao_comentario')


    models = {
        'autenticacao.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Projeto']"})
        },
        'autenticacao.doacao': {
            'Meta': {'object_name': 'Doacao'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Projeto']"}),
            'usuario_doador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Usuario']"}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        'autenticacao.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'autenticacao.perfil': {
            'Meta': {'object_name': 'Perfil'},
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Endereco']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nascimento': ('django.db.models.fields.DateField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'autenticacao.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'proposta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Proposta']"}),
            'usuario_criador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Usuario']"})
        },
        'autenticacao.proposta': {
            'Meta': {'object_name': 'Proposta'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'como_descobriu': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'data_envio': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mais_infos': ('django.db.models.fields.CharField', [], {'max_length': '700'}),
            'o_que': ('django.db.models.fields.CharField', [], {'max_length': '700'}),
            'quanto': ('django.db.models.fields.IntegerField', [], {}),
            'recompensas': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'usuario_criador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'autenticacao.usuario': {
            'Meta': {'object_name': 'Usuario', '_ormbases': ['auth.User']},
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['autenticacao']
