# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-16 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vw_question', '0009_auto_20180516_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplequestion',
            name='limit',
            field=models.FloatField(default=2),
        ),
    ]