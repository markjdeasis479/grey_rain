# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grey_rain', '0005_auto_20150220_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsubcategory',
            name='isc_desc',
            field=models.TextField(verbose_name=b'Description'),
            preserve_default=True,
        ),
    ]
