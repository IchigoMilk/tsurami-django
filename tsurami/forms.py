from django import forms

from .models import Note, Page

NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', ]

NewPageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['text', ]
    