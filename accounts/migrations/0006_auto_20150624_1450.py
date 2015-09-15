# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150624_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ask',
            options={'ordering': ['-date'], 'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='witness',
            options={'ordering': ['-date'], 'verbose_name': '\u0421\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430'},
        ),
    ]
