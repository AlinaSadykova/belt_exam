# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-18 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_trip_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='trips',
            field=models.ManyToManyField(related_name='users', to='exam_app.Trip'),
        ),
    ]
