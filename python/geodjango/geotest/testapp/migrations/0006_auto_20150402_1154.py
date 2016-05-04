# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_worldborder'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='bird_name',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bird',
            name='colony_latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='colony_location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bird',
            name='colony_longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='colony_name',
            field=models.CharField(default='colony', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='color_ring_code',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='remarks',
            field=models.CharField(default='remark', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='ring_code',
            field=models.CharField(default='code', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='sex',
            field=models.CharField(default='female', max_length=20, choices=[(b'female', b'female'), (b'male', b'male')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='tracking_end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 11, 54, 27, 550506, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='tracking_start_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 11, 54, 33, 606508, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='weight_in_g',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
