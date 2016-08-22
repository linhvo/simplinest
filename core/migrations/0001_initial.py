# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-22 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NestAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('expiration', models.DateTimeField()),
                ('client_id', models.CharField(max_length=255)),
                ('client_secret', models.CharField(max_length=255)),
                ('auth_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nest_access_token', models.CharField(max_length=255)),
                ('nest_status', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
