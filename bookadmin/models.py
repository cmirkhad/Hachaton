import datetime
from datetime import timedelta
from enum import Enum

from django.db import models
from django.db.models import TextChoices

from bookuser.models import BookUser


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
    name = models.CharField(max_length=256, default="")
    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank=True, null=True)
    category = models.ManyToManyField(Category, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=5)
    reserved_c = models.PositiveIntegerField(default=0)
    duration = models.DurationField(timedelta(days=7))

    def __str__(self):
        return self.title + " - Author: " + self.author.name+ " " +self.author.surname


class Status(TextChoices):
    RESERVED = 'RESERVED'
    TAKEN = 'TAKEN'
    EXPIRED = 'EXPIRED'
    RETURN = 'RETURN'

class ReservedBookItem(models.Model):

    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(BookUser, on_delete=models.CASCADE)
    date_from = models.DateTimeField(auto_now_add=True)
    date_to = models.DateTimeField(datetime.datetime.now()+datetime.timedelta(days=7))
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.RESERVED)


