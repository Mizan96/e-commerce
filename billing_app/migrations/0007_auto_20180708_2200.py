# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_app', '0006_auto_20180708_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]
