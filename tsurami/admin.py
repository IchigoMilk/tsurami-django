from django.contrib import admin
from django.contrib.auth.models import User
from .models import Note, Page

admin.site.register(Note)
admin.site.register(Page)
