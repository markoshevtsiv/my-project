from .models import Note
from django import forms

class NoteForm(forms.ModelForm):
    reminder = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        required=False
    )

    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']