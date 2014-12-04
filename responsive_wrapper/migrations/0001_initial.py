# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import responsive_wrapper.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsiveWrapper',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('media_queries', responsive_wrapper.fields.JSONField(editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
