# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarkuli_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='Account',
            field=models.IntegerField(),
        ),
    ]