from django import forms
from .models import Profile

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'image'
        )