from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    device = models.ForeignKey(
        'device.device', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

