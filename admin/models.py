from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField()