from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import notifications,Business,Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(max_length=50, label='email', widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
    password1 = forms.CharField(max_length=50, label='password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(max_length=50, label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']
