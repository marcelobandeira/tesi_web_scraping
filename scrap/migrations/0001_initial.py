# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-26 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questao2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=255)),
                ('gross', models.CharField(max_length=255)),
                ('gross_total', models.CharField(max_length=255)),
                ('weeks', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questao3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255, null=True)),
                ('sensation', models.CharField(max_length=255, null=True)),
                ('humidity', models.CharField(max_length=255, null=True)),
                ('pressure', models.CharField(max_length=255, null=True)),
                ('updated_at', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questao4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('density', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
