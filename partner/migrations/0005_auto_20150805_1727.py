# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_partneraddress_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partneraddress',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number', error_messages={b'invalid': 'Enter a valid phone number (ex. +999999999999).'}),
        ),
    ]
