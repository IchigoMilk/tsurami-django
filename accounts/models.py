from django.db import models
from django.contrib.auth.models import AbstractUser
from tsurami.models import Note

# Create your models here.

class User(AbstractUser):
    """カスタムユーザ"""
    aka     = models.CharField(max_length=40, verbose_name="二つ名")
    notes   = models.ManyToManyField(Note, verbose_name='ノート')
