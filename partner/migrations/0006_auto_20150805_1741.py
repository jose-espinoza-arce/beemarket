# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import partner.models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_auto_20150805_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partneraddress',
            name='phone_number',
            field=partner.models.PhoneNumberField(max_length=128, verbose_name='Phone Number', error_messages={b'invalid': 'Enter a valid phone number (ex. +999999999999).'}),
        ),
    ]
