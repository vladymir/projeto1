# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Proposta.data_envio'
        db.add_column('autenticacao_proposta', 'data_envio', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 11, 7)), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Proposta.data_envio'
        db.delete_column('autenticacao_proposta', 'data_envio')


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
