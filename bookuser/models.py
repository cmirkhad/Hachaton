from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.

class UserGroup(Group):
    def __str__(self):
        return self.name

class BookUser(AbstractUser):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    groups = models.ForeignKey(Group, models.PROTECT)
    user_permissions = None

    def __str__(self):
        return self.first_name + " " + self.last_name

