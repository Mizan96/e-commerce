# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_app', '0004_auto_20180708_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingprofilemodel',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='billingprofilemodel',
            name='card_type',
        ),
        migrations.RemoveField(
            model_name='billingprofilemodel',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='billingprofilemodel',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='billingprofilemodel',
            name='bkash_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
