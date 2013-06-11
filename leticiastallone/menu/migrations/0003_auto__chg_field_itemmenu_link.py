# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ItemMenu.link'
        db.alter_column(u'menu_itemmenu', 'link', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'ItemMenu.link'
        db.alter_column(u'menu_itemmenu', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'menu.itemmenu': {
            'Meta': {'object_name': 'ItemMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '100000'})
        }
    }

    complete_apps = ['menu']