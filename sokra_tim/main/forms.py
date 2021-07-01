from django import forms
from .models import ChangeURL


class ChangeURLForm(forms.ModelForm):
    fullurl = forms.CharField(
        label='Введите URL',
        required=True,
        error_messages={'required': ''},
        widget=forms.TextInput()
    )

    slug = forms.CharField(
        label='Введите сокращенный URL',
        required=True,
        error_messages={'required': 'hidden'},
        widget=forms.TextInput()
    )

    class Meta:
        model = ChangeURL
        fields = ['fullurl', 'slug']
