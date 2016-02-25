# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('reg_number', models.IntegerField(unique=True)),
                ('age', models.IntegerField(default=25)),
                ('address', models.TextField(max_length=1024)),
                ('physics', models.IntegerField(default=0)),
                ('chemistry', models.IntegerField(default=0)),
                ('maths', models.IntegerField(default=0)),
            ],
        ),
    ]
