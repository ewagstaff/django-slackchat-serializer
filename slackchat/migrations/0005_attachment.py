# Generated by Django 2.0.2 on 2018-02-10 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slackchat', '0004_auto_20180207_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_link', models.URLField()),
                ('text', models.TextField()),
                ('image_url', models.URLField()),
                ('image_width', models.PositiveSmallIntegerField()),
                ('image_height', models.PositiveSmallIntegerField()),
                ('service_name', models.CharField(max_length=300)),
                ('service_icon', models.URLField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.Message')),
            ],
        ),
    ]
