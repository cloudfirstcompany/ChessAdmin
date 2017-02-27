# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0018_auto_20170227_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'permissions': (('can_remove_member', 'Can remove member'), ('can_handle_join_requests', 'Can handle join requests'), ('can_handle_promotion_requests', 'Can handle promotion requests'), ('can_view_stats', 'Can view individual member stats'), ('can_create_event', 'Can create an event for this club'), ('can_add_receipt', 'Can add a receipt'), ('can_remove_receipt', 'Can remove a receipt'), ('can_access_attendance', 'Can access member attendance'), ('can_access_budget', 'Can access the budgets for this club'), ('can_create_budget', 'Can create a budget'), ('can_request_reimbusement', 'Can request for a reimbursement'), ('can_handle_reimbursement', 'Can handle reimbursement'))},
        ),
    ]
