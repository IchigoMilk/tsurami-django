from django.db import models

# Create your models here.

class User(models.Model):
  """ユーザ"""
  userid      = models.PositiveIntegerField('userid')
  name        = models.CharField('name', max_length=20)
  screen_name = models.CharField('screen-name', max_length=20)
  email       = models.EmailField('email', blank=False)
  location    = models.CharField('location', max_length=20)
  description = models.CharField('description', max_length=100)

  def __str__(self):
    return self.name
