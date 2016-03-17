# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerMaps', '0003_auto_20160215_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=10000, verbose_name=b'Url')),
                ('title', models.CharField(max_length=500, verbose_name=b'Title')),
            ],
        ),
        migrations.AlterField(
            model_name='featuredmap',
            name='image',
            field=models.ImageField(upload_to=b'static/img/FeaturedMaps/', verbose_name=b'Map'),
        ),
    ]
