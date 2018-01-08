# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-05 09:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitaltoSpecialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='HospitalSpecialization',
            new_name='Specializations',
        ),
        migrations.RenameField(
            model_name='roadblock',
            old_name='R_Severence',
            new_name='R_Duration',
        ),
        migrations.RenameField(
            model_name='specializations',
            old_name='Specialization',
            new_name='Specialisation',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='H_Specialization',
        ),
        migrations.AddField(
            model_name='roadblock',
            name='R_LastUpdatedAt',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 5, 15, 26, 49, 126987)),
        ),
        migrations.AddField(
            model_name='roadblock',
            name='R_Rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roadblock',
            name='R_Type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='hospitaltospecialization',
            name='Hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.Hospital'),
        ),
        migrations.AddField(
            model_name='hospitaltospecialization',
            name='Specialisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.Specializations'),
        ),
    ]