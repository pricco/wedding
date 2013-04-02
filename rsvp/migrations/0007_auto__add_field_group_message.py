# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.message'
        db.add_column(u'rsvp_group', 'message',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Group.message'
        db.delete_column(u'rsvp_group', 'message')


    models = {
        u'rsvp.group': {
            'Meta': {'object_name': 'Group'},
            'called': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'5HY'", 'unique': 'True', 'max_length': '3'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'age': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'attendance': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'celiac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guests'", 'to': u"orm['rsvp.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'table': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']