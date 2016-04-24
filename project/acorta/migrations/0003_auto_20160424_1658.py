# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20160421_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='urlCorta',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
