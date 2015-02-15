# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grey_rain', '0002_auto_20150208_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('caro_id', models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('caro_name', models.CharField(max_length=36, verbose_name=b'Name')),
                ('caro_desc', models.TextField(max_length=100, verbose_name=b'Description')),
                ('caro_img', models.ImageField(upload_to=b'templates/carousel', verbose_name=b'Image')),
                ('caro_link', models.URLField(verbose_name=b'Landing page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
