# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('admno', models.CharField(max_length=200)),
                ('validtill', models.DateField()),
                ('dateofbirth', models.DateField()),
                ('bloodgroup', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact1', models.CharField(max_length=10)),
                ('contact2', models.CharField(max_length=10)),
                ('photo', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
