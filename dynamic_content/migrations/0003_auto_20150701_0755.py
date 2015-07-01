# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0002_auto_20141128_0209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamiccontenttranslation',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='dynamiccontenttranslation',
            name='content_html',
            field=ckeditor.fields.RichTextField(verbose_name='Content (html)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dynamiccontenttranslation',
            name='content',
            field=models.TextField(default='', verbose_name='Content', blank=True),
            preserve_default=False,
        ),
    ]
