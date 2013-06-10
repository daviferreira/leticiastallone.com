# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'publications_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('authors', self.gf('django.db.models.fields.TextField')()),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pdf_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'publications', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'publications_article')


    models = {
        u'publications.article': {
            'Meta': {'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'authors': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pdf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['publications']