# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 21:06
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0044_auto_20170310_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='image',
            field=stdimage.models.StdImageField(default='static/media/default.jpg', upload_to=''),
        ),
    ]