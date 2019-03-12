# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-03 16:01
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin_cms', '0025_shorten_quote_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='file_hash',
            field=models.CharField(blank=True, editable=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='emailformfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type'),
        ),
    ]
