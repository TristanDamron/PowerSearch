# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerMaps', '0005_auto_20160302_1112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Featured',
        ),
    ]
