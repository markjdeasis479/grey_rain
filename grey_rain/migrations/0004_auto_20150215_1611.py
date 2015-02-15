# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grey_rain', '0003_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='caro_img',
            field=models.ImageField(upload_to=b'utopia/templates/carousel', verbose_name=b'Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_img_extra1',
            field=models.ImageField(upload_to=b'utopia/templates/item_extra_1', verbose_name=b'Image Extra 1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_img_extra2',
            field=models.ImageField(upload_to=b'utopia/templates/item_extra_2', verbose_name=b'Image Extra 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_img_extra3',
            field=models.ImageField(upload_to=b'utopia/templates/item_extra_3', verbose_name=b'Image Extra 3', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_img_lg',
            field=models.ImageField(upload_to=b'utopia/templates/item_lg', verbose_name=b'Image(Large)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_img_sm',
            field=models.ImageField(upload_to=b'utopia/templates/item_sm', verbose_name=b'Image(Small)', blank=True),
            preserve_default=True,
        ),
    ]
