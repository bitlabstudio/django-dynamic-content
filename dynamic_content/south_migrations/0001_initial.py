# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DynamicContentTranslation'
        db.create_table(u'dynamic_content_dynamiccontent_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['dynamic_content.DynamicContent'])),
        ))
        db.send_create_signal(u'dynamic_content', ['DynamicContentTranslation'])

        # Adding unique constraint on 'DynamicContentTranslation', fields ['language_code', 'master']
        db.create_unique(u'dynamic_content_dynamiccontent_translation', ['language_code', 'master_id'])

        # Adding model 'DynamicContent'
        db.create_table(u'dynamic_content_dynamiccontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'dynamic_content', ['DynamicContent'])


    def backwards(self, orm):
        # Removing unique constraint on 'DynamicContentTranslation', fields ['language_code', 'master']
        db.delete_unique(u'dynamic_content_dynamiccontent_translation', ['language_code', 'master_id'])

        # Deleting model 'DynamicContentTranslation'
        db.delete_table(u'dynamic_content_dynamiccontent_translation')

        # Deleting model 'DynamicContent'
        db.delete_table(u'dynamic_content_dynamiccontent')


    models = {
        u'dynamic_content.dynamiccontent': {
            'Meta': {'object_name': 'DynamicContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'dynamic_content.dynamiccontenttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'DynamicContentTranslation', 'db_table': "u'dynamic_content_dynamiccontent_translation'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['dynamic_content.DynamicContent']"})
        }
    }

    complete_apps = ['dynamic_content']
