# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class userModel(models.Model): 
    Firstname = models.CharField(max_length=25)
    Lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    password = models.CharField(max_length=25)
    Account = models.IntegerField()    
    Location = models.CharField(max_length=25)

    def __str__(self):
        return self.Firstname

