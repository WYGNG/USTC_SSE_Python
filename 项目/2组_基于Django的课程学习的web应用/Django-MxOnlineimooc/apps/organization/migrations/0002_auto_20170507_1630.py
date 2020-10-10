# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
