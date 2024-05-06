from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput()) 
    password = forms.CharField(widget=PasswordInput()) 



# create record

class CreateRecordForm(forms.ModelForm):

     class Meta:
        model  = Record
        fields = ['full_name', 'email', 'phone', 'state', 'lga']



# update record

class UpdateRecordForm(forms.ModelForm):

     class Meta:
        model  = Record
        fields = ['full_name', 'email', 'phone', 'state', 'lga']        