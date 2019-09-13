from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()

class NewUserForm1(UserCreationForm):
    email= forms.EmailField(required=True)
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    is_employer=forms.BooleanField()
    
    class Meta:
          model=User
        #   fields='__all__'
          fields=("first_name","last_name","username","is_employer","email","password1","password2")

    def save(self,commit=True):
        user=super(NewUserForm1,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user    

class NewUserForm2(UserCreationForm):
    email= forms.EmailField(required=True)
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    is_student=forms.BooleanField()
    

    class Meta:
          model=User
          fields=("first_name","last_name","username","is_student","email","password1","password2")

    def save(self,commit=True):
        user=super(NewUserForm2,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user            