# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ItemMenu.ordem'
        db.delete_column(u'menu_itemmenu', 'ordem')

        # Adding field 'ItemMenu.order'
        db.add_column(u'menu_itemmenu', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=100000),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ItemMenu.ordem'
        db.add_column(u'menu_itemmenu', 'ordem',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'ItemMenu.order'
        db.delete_column(u'menu_itemmenu', 'order')


    models = {
        u'menu.itemmenu': {
            'Meta': {'object_name': 'ItemMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100000'})
        }
    }

    complete_apps = ['menu']