from django import forms
#from .models import Genre
from .models import BookInCart


class AddBookToCartForm(forms.ModelForm):
  class Meta:
      model=BookInCart
      fields=(
        'book',
        'quantity',
      )