# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 08:40
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin_cms', '0010_auto_20170801_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailformfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16, verbose_name='field type'),
        ),
    ]
