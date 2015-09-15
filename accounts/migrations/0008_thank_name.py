# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_need_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='thank',
            name='name',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
