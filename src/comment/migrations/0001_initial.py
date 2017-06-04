# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 09:35
from __future__ import unicode_literals

import comment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allusers', '0002_auto_20170603_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=models.SET(comment.models.get_sentinel_user), to='allusers.AllUser')),
            ],
        ),
    ]
