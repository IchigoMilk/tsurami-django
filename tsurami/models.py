from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Note(models.Model):
    """ノート"""
    note_id     = models.PositiveIntegerField(default=0)
    created_at  = models.DateTimeField('created-date', default=timezone.now)

    # def __str__(self):
    #     return self.note_id

class Comment(models.Model):
    """コメント"""
    message_id  = models.PositiveIntegerField(default=0)
    created_at  = models.DateTimeField('created-at', default=timezone.now)
    text        = models.CharField('text', max_length=500)
    note        = models.ForeignKey(
        Note,
        on_delete=models.PROTECT,
    )
