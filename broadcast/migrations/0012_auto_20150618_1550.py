# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0011_auto_20150618_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='video',
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 12, 50, 1, 635830, tzinfo=utc)),
        ),
    ]
