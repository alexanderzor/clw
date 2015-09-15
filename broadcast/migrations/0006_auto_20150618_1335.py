# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0005_auto_20150604_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('image', models.ImageField(upload_to=b'scc/images/', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 10, 35, 53, 319302, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.OneToOneField(null=True, to='broadcast.Text'),
        ),
    ]
