# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guest.age'
        db.add_column(u'rsvp_guest', 'age',
                      self.gf('django.db.models.fields.CharField')(default='A', max_length=1),
                      keep_default=False)

        # Adding field 'Guest.listed'
        db.add_column(u'rsvp_guest', 'listed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guest.age'
        db.delete_column(u'rsvp_guest', 'age')

        # Deleting field 'Guest.listed'
        db.delete_column(u'rsvp_guest', 'listed')


    models = {
        u'rsvp.group': {
            'Meta': {'object_name': 'Group'},
            'called': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'822'", 'unique': 'True', 'max_length': '3'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'age': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'attendance': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'celiac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'child': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guests'", 'to': u"orm['rsvp.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'table': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']