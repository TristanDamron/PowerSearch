# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerMaps', '0004_auto_20160216_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img/Featured/', verbose_name=b'Featured')),
            ],
        ),
        migrations.DeleteModel(
            name='FeaturedMap',
        ),
        migrations.RemoveField(
            model_name='sites',
            name='title',
        ),
    ]
