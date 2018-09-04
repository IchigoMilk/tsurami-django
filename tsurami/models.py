import uuid
from django.db import models
from django.utils import timezone

class Note(models.Model):
    """発言の集合"""
    note_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField('created-date', default=timezone.now)
    title       = models.CharField('text', max_length=40)

    def __str__(self):
        return(str(self.note_id) + " " + self.title)

class Page(models.Model):
    """発言"""
    page_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField('created-at', default=timezone.now)
    text        = models.CharField('text', max_length=300)
    note        = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
    )

    def post(self):
        pass
    
    def __str__(self):
        return str(self.page_id)
