from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# Create your models here.



class Property(models.Model):
    name = models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    image = ImageField(blank=True, manual_crop='')
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'+ ": $" + str(self.price)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_photo', blank=True, default='profile_photo/defaultprofile.jpg')
    bio = models.CharField(max_length=255, blank=True)
    contacts = models.CharField(max_length=200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


