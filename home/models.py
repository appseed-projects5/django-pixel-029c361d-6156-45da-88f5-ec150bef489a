# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Ship Product(models.Model):

    #__Ship Product_FIELDS__
    serial number = models.CharField(max_length=255, null=True, blank=True)
    part number = models.CharField(max_length=255, null=True, blank=True)
    order number = models.CharField(max_length=255, null=True, blank=True)

    #__Ship Product_FIELDS__END

    class Meta:
        verbose_name        = _("Ship Product")
        verbose_name_plural = _("Ship Product")


class Build Kit(models.Model):

    #__Build Kit_FIELDS__
    serial number = models.CharField(max_length=255, null=True, blank=True)
    part number = models.CharField(max_length=255, null=True, blank=True)
    kit number = models.CharField(max_length=255, null=True, blank=True)

    #__Build Kit_FIELDS__END

    class Meta:
        verbose_name        = _("Build Kit")
        verbose_name_plural = _("Build Kit")



#__MODELS__END
