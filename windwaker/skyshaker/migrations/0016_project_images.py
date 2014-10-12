# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyshaker', '0015_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(to='skyshaker.Image', blank=True),
            preserve_default=True,
        ),
    ]
