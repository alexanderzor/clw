# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0010_auto_20150618_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='verbose_title',
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 18, 11, 10, 59, 906779, tzinfo=utc)),
        ),
    ]
