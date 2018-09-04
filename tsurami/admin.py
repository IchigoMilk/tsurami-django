from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

from tsurami.models import Note, Page
User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    """
    a customized user-creation-form
    """
    class Meta:
        model = User
        fields = ("username",)

class MyUserChangeForm(UserChangeForm):
    """
    a customized user-change-form
    """
    class Meta:
        model = User
        fields = '__all__'

class MyUserAdmin(UserAdmin):
    """
    a customized user-admin-form
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (None, {'fields': ('aka', 'notes')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'aka')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

admin.site.register(User, MyUserAdmin)
admin.site.register(Note)
admin.site.register(Page)
