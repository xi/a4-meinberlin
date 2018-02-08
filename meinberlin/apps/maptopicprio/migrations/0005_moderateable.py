# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-08 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import meinberlin.apps.moderatorfeedback.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin_moderatorfeedback', '0001_initial'),
        ('meinberlin_maptopicprio', '0004_make_concrete'),
    ]

    operations = [
        migrations.AddField(
            model_name='maptopic',
            name='moderator_feedback',
            field=meinberlin.apps.moderatorfeedback.fields.ModeratorFeedbackField(blank=True, choices=[('CONSIDERATION', 'Under consideration'), ('REJECTED', 'Rejected'), ('ACCEPTED', 'Accepted')], default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='maptopic',
            name='moderator_statement',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='meinberlin_moderatorfeedback.ModeratorStatement'),
        ),
    ]
