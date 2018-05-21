# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-18 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='users',
            field=models.ManyToManyField(related_name='trips', to='exam_app.User'),
        ),
    ]