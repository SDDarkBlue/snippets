# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20150402_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='remarks',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bird',
            name='tracking_end_date_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
