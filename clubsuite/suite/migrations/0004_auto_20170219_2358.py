# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0003_auto_20170219_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/'),
        ),
    ]
