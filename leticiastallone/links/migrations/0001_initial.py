# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemLink'
        db.create_table(u'links_itemlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=100000)),
            ('new_window', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'links', ['ItemLink'])


    def backwards(self, orm):
        # Deleting model 'ItemLink'
        db.delete_table(u'links_itemlink')


    models = {
        u'links.itemlink': {
            'Meta': {'object_name': 'ItemLink'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'new_window': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['links']