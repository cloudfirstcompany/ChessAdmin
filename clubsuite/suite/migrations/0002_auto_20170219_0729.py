# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 07:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('used', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('name', models.CharField(default='name for this division', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventSignIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Club')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Event')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('who_purchase', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('R', 'Requested'), ('A', 'Accepted'), ('D', 'Denied')], default='P', max_length=1)),
                ('notes', models.CharField(blank=True, max_length=1000)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('O', 'Owner'), ('A', 'Officer'), ('M', 'Member'), ('P', 'Passerby')], default='P', max_length=1)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Club')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='did',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Division'),
        ),
        migrations.AddField(
            model_name='event',
            name='did',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='suite.Division'),
            preserve_default=False,
        ),
    ]