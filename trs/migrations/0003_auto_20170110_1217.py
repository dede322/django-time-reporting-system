# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trs', '0002_auto_20170110_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project_id',
            new_name='project',
        ),
    ]