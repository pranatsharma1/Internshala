from django.forms import ModelForm

from django import forms
from datetime import datetime
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EmployerSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model=User
        fields=("company_name","username","is_employer","email","password1","password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            print("hello")
            return email
        raise forms.ValidationError('This email address is already in use.')


    def save(self,commit=True):
        print("hello")
        user=super(EmployerSignUpForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user    

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    is_student=forms.BooleanField()

    class Meta:
          model=User
          fields=("first_name","last_name","username","is_student","email","college_name","year_of_study","password1","password2")

    def clean_email(self):
            email = self.cleaned_data.get('email')
            try:
               User.objects.get(email=email)
            except User.DoesNotExist:
               return email
            raise forms.ValidationError('This email address is already in use.')


    def save(self,commit=True):
        user=super(StudentSignUpForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user   


class Job_Post(ModelForm):
    class Meta:
          model=Job
          fields=("category","job_title","location","job_duration","job_content","job_stipend")
    
    def __init__(self,user,*args,**kwargs):
        super(Job_Post,self).__init__(*args,**kwargs)


class Apply_Job(ModelForm):
    class Meta:
          model=Intern
          fields=('phone_no','college_name','username','email','basic_skills','city',"intern_name","company_name",'job_title',"job_id","hire","available")


class AcceptReject(ModelForm):
    class Meta:
        model=JobStatus
        fields=("is_accept","is_reject","intern_name","company_name",'job_title',"hire","available",)



class EditStudentProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'image',
            'college_name',
            'basic_skills',
            'city',
            'year_of_study',
        )
class EditEmployerProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields=(
            "first_name",
            "last_name",
            'email',
            'image',
            "city",
            )

class EditInternship(ModelForm):

    class Meta:
        model=Job
        fields=("category","job_title","location","job_duration","job_content","job_stipend")
