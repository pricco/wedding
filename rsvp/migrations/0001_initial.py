# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'rsvp_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(default='A5W', unique=True, max_length=3)),
            ('invited_by', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('called', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('web', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rsvp', ['Group'])

        # Adding model 'Guest'
        db.create_table(u'rsvp_guest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='guests', to=orm['rsvp.Group'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('attendance', self.gf('django.db.models.fields.CharField')(default='U', max_length=1)),
            ('diabetic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('celiac', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rsvp', ['Guest'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'rsvp_group')

        # Deleting model 'Guest'
        db.delete_table(u'rsvp_guest')


    models = {
        u'rsvp.group': {
            'Meta': {'object_name': 'Group'},
            'called': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'6KA'", 'unique': 'True', 'max_length': '3'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'attendance': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'celiac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guests'", 'to': u"orm['rsvp.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']