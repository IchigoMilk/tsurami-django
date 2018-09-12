from django import forms
# from django.contrib.auth.forms import (
#     AuthenticationForm, UserCreationForm, PasswordChangeForm,
#     PasswordResetForm, SetPasswordForm
# )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from tsurami.models import Note

User = get_user_model()

class UserSignUpForm(UserCreationForm):
    """Sign-up form"""

    class Meta:
        model = User
        # if User.USERNAME_FIELD == 'email':
        #     fields = ('email',)
        # else:
        #     fields = ('username', 'email')

        # required fields for signup
        fields = ('username', 'email', 'aka')

    def save(self, commit=True):
        user = super().save(commit=False)

        # Save prior to create relations
        if commit:
            user.save()

            # Automatically create your first Note
            note = Note.objects.create_note("new note for " + user.username)
            user.notes.add(note)

            # Maybe issues UPDATE
            user.save()

        return user

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'