from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        exclude=['seller']
class UserRegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'input-field',
        "placeholder":"input your username"
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'input-field',
        "placeholder": "input your email"
    }))
    password1=forms.CharField(label='пароль',widget=forms.PasswordInput(attrs={
         'class' : 'input-field',
         "placeholder": "enter your password"
    }))
    class Meta:
        model= User
        fields=['username','email','password1']