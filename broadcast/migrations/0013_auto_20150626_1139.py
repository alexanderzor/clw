# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0012_auto_20150618_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultant',
            options={'verbose_name': '\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date'], 'verbose_name': '\u0412\u0438\u0434\u0435\u043e'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'verbose_name': '\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0435 \u0443\u0440\u043e\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 26, 8, 39, 20, 957521, tzinfo=utc)),
        ),
    ]
