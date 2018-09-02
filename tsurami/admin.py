from django.contrib import admin
from django.contrib.auth.models import User
from .models import Note, Comment

admin.site.register(Note)
admin.site.register(Comment)
