from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from tsurami.models import Note, Page
User = get_user_model()

admin.site.register(User, UserAdmin)
admin.site.register(Note)
admin.site.register(Page)
