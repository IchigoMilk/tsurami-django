from django import forms
# from django.contrib.auth.forms import (
#     AuthenticationForm, UserCreationForm, PasswordChangeForm,
#     PasswordResetForm, SetPasswordForm
# )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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
        fields = ('username', 'email', 'aka', 'notes')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'