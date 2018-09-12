import uuid
from django.db import models
from django.utils import timezone

class NoteManager(models.Manager):
    def create_note(self, title):
        note = self.create(title=title)
        return note

class Note(models.Model):
    """発言の集合"""
    note_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField('created-date', default=timezone.now)
    title       = models.CharField('text', max_length=40, blank=False)
    # created_by  = models.IntegerField(blank=False)

    objects = NoteManager()

    def post(self):
        pass

    def __str__(self):
        return(self.title)

class PageManager(models.Manager):
    def create_page(self, text, note):
        page = self.create(text=text, note=note)
        return page

class Page(models.Model):
    """発言"""
    page_id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField('created-at', default=timezone.now)
    text        = models.CharField('text', max_length=300, blank=False)
    note        = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
    )

    objects = PageManager()

    def __str__(self):
        return str(self.page_id)
