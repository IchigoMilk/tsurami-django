from django.contrib import admin
from .models import Note, Message, User

admin.site.register(Note)
admin.site.register(Message)
admin.site.register(User)
