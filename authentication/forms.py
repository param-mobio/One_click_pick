from django import forms
from django.forms import ModelForm
from user.models import User

class Registerform(ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    password1 = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'************'}))
    password2 = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'*************'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']
