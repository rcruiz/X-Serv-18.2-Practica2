# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0003_auto_20160424_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='urlCorta',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
