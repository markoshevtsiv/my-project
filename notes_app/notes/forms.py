from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']