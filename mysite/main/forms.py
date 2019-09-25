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
          fields=('phone_no',"intern_name","company_name",'job_title',"job_id","hire","available","document")

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
          fields=("first_name","last_name","username","is_employer","email","image","password1","password2")

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

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'image',
            'password',
        )














 
                                                    # Mahima's Code

# =======
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.db import models
# from . models import profile,skillcategory
# from django.db import models


# class profileform(ModelForm):
#     class Meta :
#         model = profile
#         fields = ("name","skill","college","phone_no","location","company_name")



# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     last_name = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=100)
#     #differ_id = forms.CharField(required=True, label="Differ_Id")


#     class Meta:
#         model = User
#         fields = ("first_name","last_name","username","email","password1","password2")

#     def save(self, commit=True):
#         user = super(NewUserForm,self).save(commit=False)
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()
#         return user    


# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d
