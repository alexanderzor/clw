# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150603_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='my_asks', to='accounts.CustomUser', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Witness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='my_witnesses', to='accounts.CustomUser', null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='need',
            options={'ordering': ['-date'], 'verbose_name': '\u041d\u0443\u0436\u0434\u044b'},
        ),
        migrations.AlterModelOptions(
            name='thank',
            options={'ordering': ['-date'], 'verbose_name': '\u0411\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u043d\u043e\u0441\u0442\u0438'},
        ),
    ]
