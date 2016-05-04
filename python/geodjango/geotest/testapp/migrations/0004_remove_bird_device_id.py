# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_log_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bird',
            name='device_id',
        ),
    ]
