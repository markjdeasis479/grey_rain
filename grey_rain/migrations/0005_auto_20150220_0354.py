# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grey_rain', '0004_auto_20150215_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_short_desc',
            field=models.CharField(max_length=100, verbose_name=b'Short Description'),
            preserve_default=True,
        ),
    ]
