# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-16 12:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vw_question', '0007_auto_20180516_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]