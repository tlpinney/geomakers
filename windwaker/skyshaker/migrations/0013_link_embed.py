# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyshaker', '0012_auto_20141011_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='embed',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
