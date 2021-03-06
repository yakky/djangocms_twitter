# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TwitterRecentEntries.twitter_id'
        db.add_column('cmsplugin_twitterrecententries', 'twitter_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75),
                      keep_default=False)

        # Adding field 'TwitterSearch.twitter_id'
        db.add_column('cmsplugin_twittersearch', 'twitter_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TwitterRecentEntries.twitter_id'
        db.delete_column('cmsplugin_twitterrecententries', 'twitter_id')

        # Deleting field 'TwitterSearch.twitter_id'
        db.delete_column('cmsplugin_twittersearch', 'twitter_id')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 23, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'djangocms_twitter.twitterrecententries': {
            'Meta': {'object_name': 'TwitterRecentEntries', 'db_table': "'cmsplugin_twitterrecententries'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'link_hint': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'twitter_user': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'djangocms_twitter.twittersearch': {
            'Meta': {'object_name': 'TwitterSearch', 'db_table': "'cmsplugin_twittersearch'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'query': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['djangocms_twitter']