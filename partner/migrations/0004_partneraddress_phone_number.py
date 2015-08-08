# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_auto_20150604_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='partneraddress',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+9999999999', max_length=128, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]
