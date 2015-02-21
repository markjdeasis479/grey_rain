# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grey_rain', '0006_auto_20150220_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessionizer',
            fields=[
                ('session_id', models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('session_token', models.CharField(max_length=32, verbose_name=b'Token')),
                ('session_date_time_created', models.DateTimeField(auto_now=True, verbose_name=b'Date/ Time created')),
                ('session_date_time_expired', models.DateTimeField(verbose_name=b'Date/ Time expired', blank=True)),
                ('session_user', models.ForeignKey(to='grey_rain.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
