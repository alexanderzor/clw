# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0006_auto_20150618_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 10, 52, 43, 224479, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.ForeignKey(to='broadcast.Text', null=True),
        ),
    ]
