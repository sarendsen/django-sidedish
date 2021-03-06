# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Dish.pages'
        db.alter_column(u'sidedish_dish', 'pages', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Dish.side'
        db.alter_column(u'sidedish_dish', 'side', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

    def backwards(self, orm):

        # Changing field 'Dish.pages'
        db.alter_column(u'sidedish_dish', 'pages', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Dish.side'
        db.alter_column(u'sidedish_dish', 'side', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    models = {
        u'sidedish.dish': {
            'Meta': {'ordering': "['weight', '-created_at']", 'object_name': 'Dish'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '500'})
        }
    }

    complete_apps = ['sidedish']
