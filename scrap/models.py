# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Questao1(models.Model):
	movie = models.CharField(max_length = 255)
	rating = models.CharField(max_length = 255)	

class Questao2(models.Model):
	movie = models.CharField(max_length = 255)
	gross = models.CharField(max_length = 255)
	gross_total = models.CharField(max_length = 255)
	weeks = models.CharField(max_length = 255)


class Questao3(models.Model):
	temperature = models.CharField(max_length = 255, null = False)
	condition = models.CharField(max_length = 255, null = True)
	sensation = models.CharField(max_length = 255, null = True)
	humidity = models.CharField(max_length = 255, null = True)
	pressure = models.CharField(max_length = 255, null = True)
	updated_at = models.CharField(max_length = 255, null = True)

class Questao4(models.Model):
	country = models.CharField(max_length = 255, null = False)
	density = models.FloatField(null=True)