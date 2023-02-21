from django import forms
from django.forms import ModelForm
from user.models import User
from django.contrib.auth.forms import UserCreationForm  


class Registerform(ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name','required':'True'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your last name','required':'True'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email','required':'True'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'************','required':'True'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'*************','required':'True'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','confirm_password']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        for i in first_name:

            if(i.isdigit()):
                raise forms.ValidationError('first name contains only alphabet')
            if(i=='@' or i=='#'or i=='%'or i=='&'):
                raise forms.ValidationError('first name contains only alphabet')
        return first_name    

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        for i in last_name:

            if(i.isdigit()):
                raise forms.ValidationError('last name contains only alphabet')
            if(i=='@' or i=='#' or i=='%' or i=='&'):
                raise forms.ValidationError('last name contains only alphabet')
        return last_name
            
    def clean_password(self):
        password = self.cleaned_data['password']
        print('pasword',password)
        # confirm_password = self.cleaned_data['confirm_password']
        # print('conpassword',confirm_password)
        if(len(password)<8):
            raise forms.ValidationError('password must contain more than 8 character')
        else:
            l, u, p, d = 0, 0, 0, 0
            for i in password:
                # counting lowercase alphabets
                if (i.islower()):
                    l += 1

                # counting uppercase alphabets
                if (i.isupper()):
                    u += 1

                # counting digits
                if (i.isdigit()):
                    d += 1

                # counting the mentioned special characters
                if (i == '@' or i == '$' or i == '_'):
                    p += 1
            if (l < 1 or u < 1 or p < 1 or d < 1 or l+p+u+d != len(password)):
                raise forms.ValidationError('password must be strong')
        # if(password!=confirm_password):
        #     raise forms.ValidationError('password must be same')
        
        return password
    
    # def clean_confirm_password(self):
    #     cleaned_data =  super().clean()
    #     confirm_password = cleaned_data['confirm_password']
    #     passw = cleaned_data['password']
    #     print('passw',passw)
        # password = cleaned_data['password']
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            msg = 'confirm password does not match'
            self.add_error('confirm_password',msg)
        return self.cleaned_data
        

    

# class Loginform(forms.Form):
#     email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email', 'name':'email'}))
#     password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'************','name':'password'}))
