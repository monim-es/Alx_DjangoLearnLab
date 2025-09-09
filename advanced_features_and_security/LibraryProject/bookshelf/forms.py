from django import forms
from .models import Book

# ExampleForm (used for the check)
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
