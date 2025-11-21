from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Book, Notes


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'pages', 'available']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }

class NotesForm(forms.ModelForm):
    reminder = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}),
        required=False,
    )

    class Meta:
        model = Notes
        fields = ['title', 'text', 'reminder']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']