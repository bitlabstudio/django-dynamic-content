# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DynamicContentTranslation.content_html'
        db.add_column(u'dynamic_content_dynamiccontent_translation', 'content_html',
                      self.gf('ckeditor.fields.RichTextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'DynamicContentTranslation.content'
        db.alter_column(u'dynamic_content_dynamiccontent_translation', 'content', self.gf('django.db.models.fields.TextField')(default=''))

    def backwards(self, orm):
        # Deleting field 'DynamicContentTranslation.content_html'
        db.delete_column(u'dynamic_content_dynamiccontent_translation', 'content_html')


        # Changing field 'DynamicContentTranslation.content'
        db.alter_column(u'dynamic_content_dynamiccontent_translation', 'content', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'dynamic_content.dynamiccontent': {
            'Meta': {'unique_together': '()', 'object_name': 'DynamicContent', 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        u'dynamic_content.dynamiccontenttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'DynamicContentTranslation', 'db_table': "u'dynamic_content_dynamiccontent_translation'", 'index_together': '()'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_html': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['dynamic_content.DynamicContent']"})
        }
    }

    complete_apps = ['dynamic_content']