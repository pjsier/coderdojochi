# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 21:37
from __future__ import unicode_literals

import coderdojochi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0003_auto_20160426_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=coderdojochi.models.generate_filename),
        ),
    ]
