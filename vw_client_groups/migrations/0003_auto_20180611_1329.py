# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 10:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vw_client_groups', '0002_auto_20180611_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientgroup',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='General client'),
        ),
        migrations.AlterField(
            model_name='subclientgroup',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
    ]
