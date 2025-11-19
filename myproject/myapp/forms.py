from django import forms

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
