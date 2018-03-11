# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='times',
            field=models.IntegerField(choices=[(1, '8:00'), (2, '9:00'), (3, '10:00'), (4, '11:00'), (5, '13:00'), (6, '14:00'), (7, '15:00'), (8, '16:00'), (9, '17:00')], verbose_name='时间段'),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('data', 'times', 'meeting_room')]),
        ),
    ]