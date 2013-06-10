# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemMenu'
        db.create_table(u'menu_itemmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('ordem', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'menu', ['ItemMenu'])


    def backwards(self, orm):
        # Deleting model 'ItemMenu'
        db.delete_table(u'menu_itemmenu')


    models = {
        u'menu.itemmenu': {
            'Meta': {'object_name': 'ItemMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'ordem': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['menu']