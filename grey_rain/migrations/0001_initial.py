# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(serialize=False, primary_key=True)),
                ('cust_email', models.CharField(max_length=32, verbose_name=b'Email Address')),
                ('cust_password', models.CharField(max_length=32, verbose_name=b'Password')),
                ('cust_prefix', models.CharField(max_length=10, verbose_name=b'Prefix', choices=[(b'Mr.', b'Mr.'), (b'Ms.', b'Ms.'), (b'Mrs.', b'Mrs.')])),
                ('cust_first_name', models.CharField(max_length=32, verbose_name=b'First Name')),
                ('cust_middle_name', models.CharField(max_length=32, verbose_name=b'Middle Name')),
                ('cust_last_name', models.CharField(max_length=32, verbose_name=b'Last Name')),
                ('cust_gender', models.CharField(max_length=10, verbose_name=b'Gender', choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('cust_birth_date', models.DateField(verbose_name=b'Birth date')),
                ('cust_phone_number', models.CharField(max_length=20, verbose_name=b'Phone Number')),
                ('cust_alt_phone', models.CharField(max_length=20, verbose_name=b'Alt. Phone Number')),
                ('cust_home_address', models.CharField(max_length=64, verbose_name=b'Home Address')),
                ('cust_alt_home', models.CharField(max_length=64, verbose_name=b'Provincial Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
