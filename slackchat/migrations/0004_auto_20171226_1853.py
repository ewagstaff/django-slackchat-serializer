# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsoneditor.fields.postgres_jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('slackchat', '0003_auto_20171222_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='markupcontent',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='slackchat.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='markupcontent',
            name='content',
            field=jsoneditor.fields.postgres_jsonfield.JSONField(),
        ),
        migrations.AlterField(
            model_name='messagemarkup',
            name='content_template',
            field=jsoneditor.fields.postgres_jsonfield.JSONField(),
        ),
    ]
