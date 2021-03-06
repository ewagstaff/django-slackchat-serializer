# Generated by Django 2.0.2 on 2018-03-19 01:15

import uuid

import django.db.models.deletion
import django.utils.timezone
import slackchat.conf
import slackchat.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(help_text='The name of the argument that will be attached to a          message.', max_length=255)),
                ('character', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('title_link', models.URLField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('service_name', models.CharField(blank=True, max_length=300, null=True)),
                ('service_icon', models.URLField(blank=True, null=True)),
                ('service_url', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('image_width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image_height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('video_html', models.TextField(blank=True, null=True)),
                ('video_html_width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('video_html_height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('thumb_url', models.URLField(blank=True, null=True)),
                ('thumb_width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('thumb_height', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('api_id', models.SlugField(blank=True, editable=False, help_text='Slack API channel ID', max_length=10, null=True)),
                ('team_id', models.SlugField(blank=True, editable=False, help_text='Slack API team ID', max_length=10, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('introduction', slackchat.fields.MarkdownField(blank=True, help_text='Some introductory paragraph text (in markdown syntax).', null=True)),
                ('meta_title', models.CharField(blank=True, help_text='Page title', max_length=300, null=True)),
                ('meta_description', models.CharField(blank=True, help_text='Page description', max_length=300, null=True)),
                ('meta_image', models.URLField(blank=True, help_text='Share image URL', null=True)),
                ('publish_path', models.CharField(blank=True, help_text="A relative path you can use when         publishing the slackchat, e.g.,         <span style='color:grey; font-weight:bold;'>/2018-02-12/econ-chat/        </span>.", max_length=300, unique=True)),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, help_text='Dateline.')),
                ('live', models.BooleanField(default=False, help_text='Determines whether page should re-poll for new messages         while chat is live.')),
            ],
        ),
        migrations.CreateModel(
            name='ChatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255)),
                ('publish_path', models.CharField(default='/slackchats/', help_text="A relative path for the slackchat type         you can append to any slackchat channel's         publish path, e.g.,         <span style='color:grey; font-weight:bold;'>/slackchats/        </span>.", max_length=300)),
                ('render_to_html', models.BooleanField(default=False, help_text='Whether to render markdown to HTML in the serializer.')),
                ('kwargs_in_threads', models.BooleanField(default=True, help_text='Whether users can create kwargs in threads.')),
            ],
        ),
        migrations.CreateModel(
            name='CustomContentTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('argument_name', models.SlugField(blank=True, help_text="Add an argument to the message if search_string         matches against a message's content.", max_length=255, null=True)),
                ('search_string', models.CharField(help_text='A regex search string with capture groups.', max_length=255)),
                ('content_template', models.TextField(help_text='A Python format string whose args are the capture groups         matched by the search_string.')),
                ('chat_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.ChatType')),
            ],
        ),
        migrations.CreateModel(
            name='KeywordArgument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('key', models.SlugField(max_length=30)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('text', models.TextField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='slackchat.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('reaction', models.CharField(max_length=150)),
                ('argument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slackchat.Argument')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='slackchat.Message')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(upload_to=slackchat.conf.default_user_image_upload_to)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.URLField(unique=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='reaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='keywordargument',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kwargs', to='slackchat.Message'),
        ),
        migrations.AddField(
            model_name='keywordargument',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='channel',
            name='chat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='slackchat.ChatType'),
        ),
        migrations.AddField(
            model_name='channel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='slackchat.User'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='slackchat.Message'),
        ),
        migrations.AddField(
            model_name='argument',
            name='chat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackchat.ChatType'),
        ),
        migrations.AlterUniqueTogether(
            name='attachment',
            unique_together={('message', 'title_link', 'image_url')},
        ),
    ]
