# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-16 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vw_question', '0010_samplequestion_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplequestion',
            name='limit',
            field=models.IntegerField(default=2),
        ),
    ]
