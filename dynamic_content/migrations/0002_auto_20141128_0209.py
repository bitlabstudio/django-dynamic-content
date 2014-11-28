# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamiccontent',
            name='identifier',
            field=models.CharField(unique=True, max_length=256, verbose_name=b'Unique identifier'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dynamiccontenttranslation',
            name='content',
            field=models.TextField(null=True, verbose_name='Content', blank=True),
            preserve_default=True,
        ),
    ]
