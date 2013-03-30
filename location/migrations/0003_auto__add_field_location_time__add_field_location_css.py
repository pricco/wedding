# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.time'
        db.add_column(u'location_location', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Location.css'
        db.add_column(u'location_location', 'css',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.time'
        db.delete_column(u'location_location', 'time')

        # Deleting field 'Location.css'
        db.delete_column(u'location_location', 'css')


    models = {
        u'location.location': {
            'Meta': {'object_name': 'Location'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'css': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '10'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['location']