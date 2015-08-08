# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import partner.models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_auto_20150805_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partneraddress',
            name='phone_number',
            field=partner.models.PhoneNumberField(max_length=128, verbose_name='Phone Number'),
        ),
    ]
