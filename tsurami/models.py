import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Note(models.Model):
    """ノート"""
    note_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField('created-date', default=timezone.now)

    def __str__(self):
        return str(self.note_id)

class Page(models.Model):
    """コメント"""
    page_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField('created-at', default=timezone.now)
    text        = models.CharField('text', max_length=500)
    note        = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.page_id)
