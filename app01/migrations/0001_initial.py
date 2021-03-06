# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='会议室名')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='日期')),
                ('times', models.IntegerField(choices=[(1, '8:00'), (1, '9:00'), (1, '10:00'), (1, '11:00'), (1, '13:00'), (1, '14:00'), (1, '15:00'), (1, '16:00'), (1, '17:00')], verbose_name='时间段')),
                ('meeting_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Meeting_room')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
    ]
