# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-16 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20191016_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default=b'', max_length=255, null=True, upload_to=b'images/'),
        ),
    ]