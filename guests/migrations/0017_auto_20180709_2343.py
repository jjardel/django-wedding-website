# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-09 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_party_rehearsal_dinner'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='interested_in_bus',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='meal',
            field=models.CharField(blank=True, choices=[('omnivore', 'I eat anything'), ('vegetarian', 'Veggies only, please'), ('vegan', 'No animal products for me')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='type',
            field=models.CharField(choices=[('default', 'default')], max_length=10),
        ),
    ]
