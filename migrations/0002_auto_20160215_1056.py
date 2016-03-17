# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerMaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredmap',
            name='image',
            field=models.ImageField(upload_to=b'img/Featured Maps/', verbose_name=b'Map'),
        ),
    ]
