from django.db import models


class Location(models.Model):

    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='location/icon', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)
    active = models.BooleanField(default=True)