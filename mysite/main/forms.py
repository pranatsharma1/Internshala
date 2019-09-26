from django.forms import ModelForm

from django import forms
from datetime import datetime
from .models import Job,Intern
from django.contrib.auth.forms import UserCreationForm,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()




# class Category(ModelForm):
#     class Meta:
#         model=Category
#         fields=("category",)

# class Location(ModelForm):
#     class Meta:
#         model=Location
#         fields=("location",)


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Apply_Job(ModelForm):
    class Meta:
          model=Intern
          fields=("intern_name","job_title","company_name","intern_college","intern_skills","intern_city","intern_study_year")

class Job_Post(ModelForm):
    class Meta:
          model=Job
          fields=("category","job_title","location","job_duration","job_content","job_published","job_stipend")
    
    def __init__(self,user,*args,**kwargs):
        super(Job_Post,self).__init__(*args,**kwargs)

class NewUserForm1(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100) 
    is_employer=forms.BooleanField()
    

    class Meta:
          model=User
        #   fields='__all__'
          fields=("first_name","last_name","username","is_employer","email","city","image","password1","password2")

    def save(self,commit=True):
        user=super(NewUserForm1,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user    

class NewUserForm2(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    is_student=forms.BooleanField()
    image=forms.ImageField()

    class Meta:
          model=User
          fields=("first_name","last_name","username","is_student","email","image","college_name","city","year_of_study","basic_skills","password1","password2")

    def save(self,commit=True):
        user=super(NewUserForm2,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user   

class EditStudentProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'college_name',
            'basic_skills',
            'city',
            'year_of_study',
        )
class EditEmployerProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'city',
        )        
