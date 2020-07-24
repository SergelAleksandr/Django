from .models import CommentsBook
from django import forms

class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsBook
        fields = ('user', 'body',)

