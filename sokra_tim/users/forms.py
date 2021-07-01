from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserOurRegistraion(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


    def __init__(self, *args, **kwargs):
        super(UserOurRegistraion, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']
