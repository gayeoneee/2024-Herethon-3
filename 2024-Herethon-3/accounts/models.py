from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUsers(AbstractUser):
    nickname = models.CharField(max_length=15)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')
