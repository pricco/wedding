from django.db import models


class Song(models.Model):

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    path = models.FileField(upload_to='music/song')
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    tag = models.CharField(max_length=40, null=True, blank=True)