from django.db import models
class Songs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    is_artist = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    is_top = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
