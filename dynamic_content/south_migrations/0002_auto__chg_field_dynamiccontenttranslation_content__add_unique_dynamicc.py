# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DynamicContentTranslation.content'
        db.alter_column(u'dynamic_content_dynamiccontent_translation', 'content', self.gf('django.db.models.fields.TextField')(null=True))
        # Adding unique constraint on 'DynamicContent', fields ['identifier']
        db.create_unique(u'dynamic_content_dynamiccontent', ['identifier'])


    def backwards(self, orm):
        # Removing unique constraint on 'DynamicContent', fields ['identifier']
        db.delete_unique(u'dynamic_content_dynamiccontent', ['identifier'])


        # User chose to not deal with backwards NULL issues for 'DynamicContentTranslation.content'
        raise RuntimeError("Cannot reverse this migration. 'DynamicContentTranslation.content' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'DynamicContentTranslation.content'
        db.alter_column(u'dynamic_content_dynamiccontent_translation', 'content', self.gf('django.db.models.fields.TextField')())

    models = {
        u'dynamic_content.dynamiccontent': {
            'Meta': {'object_name': 'DynamicContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        u'dynamic_content.dynamiccontenttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'DynamicContentTranslation', 'db_table': "u'dynamic_content_dynamiccontent_translation'"},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['dynamic_content.DynamicContent']"})
        }
    }

    complete_apps = ['dynamic_content']
