# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20150716_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvedcourselist',
            name='ELECT',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
    ]
