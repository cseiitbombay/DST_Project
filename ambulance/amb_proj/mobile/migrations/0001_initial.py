# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-05 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_Name', models.CharField(max_length=200)),
                ('H_Phone', models.IntegerField(default=0)),
                ('H_Email', models.EmailField(max_length=50)),
                ('H_Address', models.CharField(max_length=300)),
                ('H_Latitude', models.FloatField(default=0.0)),
                ('H_Longitude', models.FloatField(default=0.0)),
                ('H_Specialization', models.CharField(max_length=200)),
                ('H_LastUpdatedAt', models.DateTimeField(verbose_name='last updated')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalSpecialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specialization', models.CharField(max_length=50)),
                ('S_LastUpdatedAt', models.DateTimeField(verbose_name='last updated')),
            ],
        ),
        migrations.CreateModel(
            name='RoadBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_Latitude', models.FloatField(default=0.0)),
                ('R_Longitude', models.FloatField(default=0.0)),
                ('R_Severence', models.IntegerField(default=0)),
            ],
        ),
    ]
