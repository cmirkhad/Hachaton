from datetime import timedelta

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    def __str__(self):
        return self.name + " " + self.surname

class Publisher(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank=True, null=True)
    category = models.ManyToManyField(Category, null=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=5)
    reserved_c = models.PositiveIntegerField(default=0)
    duration = models.DurationField(timedelta(days=7))

    def __str__(self):
        return self.title + " - Author: " + self.author.name+ " " +self.author.surname

