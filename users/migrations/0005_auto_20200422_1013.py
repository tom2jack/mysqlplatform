# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-22 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170827_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagerecord',
            name='click_path',
            field=models.CharField(default='/', max_length=100, verbose_name='\u8df3\u8f6c\u8def\u5f84'),
        ),
        migrations.AddField(
            model_name='messagerecord',
            name='is_read',
            field=models.IntegerField(default=0, verbose_name='\u672a\u8bfb\u72b6\u6001'),
        ),
    ]