# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0003_auto_20141104_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='client_id',
            field=models.CharField(default=None, max_length=100, db_index=True),
            preserve_default=False,
        ),
    ]
