# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 08:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0015_merge_20170226_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(through='suite.Role', to=settings.AUTH_USER_MODEL),
        ),
    ]
