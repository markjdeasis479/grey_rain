# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grey_rain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_code', models.CharField(max_length=8, verbose_name=b'Code')),
                ('item_name', models.CharField(max_length=32, verbose_name=b'Name')),
                ('item_price', models.DecimalField(default=0.0, verbose_name=b'Price', max_digits=10, decimal_places=2)),
                ('item_short_desc', models.CharField(max_length=32, verbose_name=b'Short Description')),
                ('item_long_desc', models.TextField(verbose_name=b'Long Description')),
                ('item_date_added', models.DateField(auto_now=True, verbose_name=b'Date Added')),
                ('item_rental_day', models.IntegerField(verbose_name=b'Rental Day')),
                ('item_img_sm', models.ImageField(upload_to=b'templates/item_sm', verbose_name=b'Image(Small)', blank=True)),
                ('item_img_lg', models.ImageField(upload_to=b'templates/item_lg', verbose_name=b'Image(Large)', blank=True)),
                ('item_img_extra1', models.ImageField(upload_to=b'templates/item_extra_1', verbose_name=b'Image Extra 1', blank=True)),
                ('item_img_extra2', models.ImageField(upload_to=b'templates/item_extra_2', verbose_name=b'Image Extra 2', blank=True)),
                ('item_img_extra3', models.ImageField(upload_to=b'templates/item_extra_3', verbose_name=b'Image Extra 3', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('ic_id', models.AutoField(serialize=False, primary_key=True)),
                ('ic_name', models.CharField(max_length=32, verbose_name=b'Name')),
                ('ic_desc', models.TextField(verbose_name=b'Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemSubcategory',
            fields=[
                ('isc_id', models.AutoField(serialize=False, primary_key=True)),
                ('isc_name', models.CharField(max_length=32, verbose_name=b'Name')),
                ('isc_desc', models.TextField(max_length=32, verbose_name=b'Description')),
                ('isc_category', models.ForeignKey(to='grey_rain.ItemCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemVariant',
            fields=[
                ('ivar_id', models.AutoField(serialize=False, primary_key=True)),
                ('ivar_size', models.CharField(max_length=20, verbose_name=b'Size', choices=[(b'Extra Small', b'Extra Small'), (b'Small', b'Small'), (b'Medium', b'Medium'), (b'Large', b'Large'), (b'Extra Large', b'Extra Large')])),
                ('ivar_color', models.CharField(max_length=36, verbose_name=b'Color', blank=True)),
                ('ivar_qty', models.IntegerField(default=0, verbose_name=b'Quantity')),
                ('ivar_item', models.ForeignKey(to='grey_rain.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='item_subcategory',
            field=models.ForeignKey(to='grey_rain.ItemSubcategory'),
            preserve_default=True,
        ),
    ]
