from datetime import timedelta

from django.db import models

<<<<<<< HEAD

class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    publisher = models.CharField(max_length=256)
    # category = models.ForeignKey('Category')
    # author = models.ForeignKey('Author')
    count = models.PositiveIntegerField()
    reserved_c = models.PositiveIntegerField()
||||||| 276dac3
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to=)
    publisher = models.CharField(max_length=256)
    category = models.ForeignKey('Category')
    author = models.ForeignKey('Author')
    count = models.PositiveIntegerField()
    reserved_c = models.PositiveIntegerField()
=======
# Create your models here.
>>>>>>> mirkhad


class Author(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
<<<<<<< HEAD
||||||| 276dac3

=======

class Publisher(models.Model):
    name = models.CharField(max_length=256)


class Category(models.Model):
    name = models.CharField(max_length=256)



class Books(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='/')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank=True, null=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=5)
    reserved_c = models.PositiveIntegerField(default=0)
    duration = models.DurationField(timedelta(days=7))



>>>>>>> mirkhad
