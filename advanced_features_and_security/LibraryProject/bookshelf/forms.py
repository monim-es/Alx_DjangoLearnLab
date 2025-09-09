from django import forms
from .models import Book

# Form for creating/updating books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']