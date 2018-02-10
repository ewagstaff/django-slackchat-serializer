# Generated by Django 2.0.2 on 2018-02-10 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slackchat', '0005_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='slackchat.Message'),
        ),
    ]
