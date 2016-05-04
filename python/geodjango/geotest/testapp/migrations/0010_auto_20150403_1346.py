# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_auto_20150403_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='colony_location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True),
            preserve_default=True,
        ),
    ]
