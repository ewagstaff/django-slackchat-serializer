# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slackchat', '0011_auto_20171228_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custommessagetemplate',
            name='regex',
        ),
    ]
