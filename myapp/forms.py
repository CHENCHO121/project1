from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'UserName'}))

    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2',)


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['user','bio','phone_no','dob','profile_img']
