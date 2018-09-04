from django.db import models
from django.contrib.auth.models import AbstractUser
from tsurami.models import Note

# Create your models here.

class User(AbstractUser):
    """カスタムユーザ"""
    aka     = models.CharField('text', max_length=40)
    notes   = models.ManyToManyField(Note, verbose_name='ノート')
