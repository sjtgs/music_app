# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-10 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_songtype_artistnames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songtype',
            name='ArtistNames',
        ),
    ]
