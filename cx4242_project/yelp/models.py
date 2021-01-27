# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    stars = models.CharField(max_length=4)

class Stems(models.Model):
    word = models.CharField(max_length=16)
    stem = models.CharField(max_length=16)

class 
