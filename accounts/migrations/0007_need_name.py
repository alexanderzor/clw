# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150624_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='name',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
