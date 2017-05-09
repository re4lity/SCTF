# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_team_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Team'),
        ),
    ]