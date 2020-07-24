from django import forms
from .models import Books

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = (
            'name',
            'author',
            'description',
            'genre',
            'price',
            'image',
            'year',
            'quantity',
            'binding',
            'forma',
            'isbn',
            'weight',
            'age',
            'publisher',
            'rate',
        )
