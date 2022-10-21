from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    publisher = models.CharField(max_length=256)
    count = models.PositiveIntegerField()
    reserved_c = models.PositiveIntegerField()


class Author(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
