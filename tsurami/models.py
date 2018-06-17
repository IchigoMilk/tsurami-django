from django.db import models
from django.utils import timezone

class Note(models.Model):
  """ノート"""
  note_id     = models.PositiveIntegerField(default=0)
  created_at  = models.DateTimeField('created-date', default=timezone.now)

  # def __str__(self):
  #   return self.note_id

class Message(models.Model):
  """コメント"""
  message_id  = models.PositiveIntegerField(default=0)
  created_at  = models.DateTimeField('created-at', default=timezone.now)
  text        = models.CharField('text', max_length=500)
  note        = models.ForeignKey(
    Note,
    on_delete=models.PROTECT,
    )

class User(models.Model):
  """ユーザ"""
  user_id     = models.PositiveIntegerField(default=0)
  name        = models.CharField('name', max_length=20, default="noname")
  screen_name = models.CharField('screen-name', max_length=20)
  email       = models.EmailField('email', blank=False)
  location    = models.CharField('location', max_length=20)
  description = models.CharField('description', max_length=100)
  created_at  = models.DateTimeField('registration-date', default=timezone.now)
  note        = models.OneToOneField(
    Note,
    verbose_name='Note',
    on_delete=models.PROTECT,
    )

  def __str__(self):
    return self.name
