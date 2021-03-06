# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-28 07:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vw_client_groups', '0004_auto_20180628_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientgroup',
            name='companies',
        ),
        migrations.AddField(
            model_name='clientgroup',
            name='admins',
            field=models.ManyToManyField(related_name='companies', to=settings.AUTH_USER_MODEL, verbose_name='Admins of company'),
        ),
    ]
