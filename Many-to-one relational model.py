from django.db import models
  
class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
  
class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
