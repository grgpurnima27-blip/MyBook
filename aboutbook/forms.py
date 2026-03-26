from django import forms
from .models import Book
class create (forms.ModelForm):
    class Meta:
        model = Book
        fields =['title', 'author', 'description','price']
