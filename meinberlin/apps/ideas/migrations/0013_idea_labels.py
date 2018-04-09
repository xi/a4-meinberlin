# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4labels', '0001_initial'),
        ('meinberlin_ideas', '0012_add_form_hint_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='labels',
            field=models.ManyToManyField(related_name='meinberlin_ideas_idea_label', to='a4labels.Label'),
        ),
    ]
