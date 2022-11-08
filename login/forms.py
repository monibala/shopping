from dataclasses import fields
from pyexpat import model

from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation
# from matplotlib import widgets
from home.models import Customer
# from matplotlib import widgets

class CustomerRegistrationForm(UserCreationForm):
    email = forms.CharField(label='Email',required=True , widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    # email = forms.CharField(label='Email',required=True , widget=forms.EmailInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','auto-focus':'True','class':'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
   

class MyPasswordRestForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))    


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
   

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name' ,'locality' ,'mobile','city','state','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                    'locality':forms.TextInput(attrs={'class':'form-control'}),
                    'mobile':forms.NumberInput(attrs={'class':'form-control'}),

                    'city':forms.TextInput(attrs={'class':'form-control'}), 
                    'state':forms.Select(attrs={'class':'form-control'}),
                    'zipcode':forms.NumberInput(attrs={'class':'form-control'})
                    }