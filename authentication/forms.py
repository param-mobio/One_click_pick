from django import forms
from django.forms import ModelForm
from user.models import User
from django.contrib.auth.forms import UserCreationForm  


class Registerform(ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'************'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'*************'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','confirm_password']

# class Loginform(forms.Form):
#     email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email', 'name':'email'}))
#     password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'************','name':'password'}))
