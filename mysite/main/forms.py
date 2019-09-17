from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from . models import UserProfile,IntershipCategory,post_job
from django.contrib.auth.models import User,AbstractUser
from .models import Category, Products,Location


User=get_user_model()

class NewUserForm1(UserCreationForm):
    email= forms.EmailField(required=True)
    last_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    is_employer=forms.BooleanField()
    
    class Meta:
          model=User
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


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )    

#new code

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user',  'city', 'phone', 'website')


class EmployerForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'company_name','company_location', 'phone', 'website')

#new 

class IntershipCategoryForm(forms.ModelForm):
    class Meta:
        model = IntershipCategory
        fields = ('intership_category','intership_summray')

class HomeForm(forms.ModelForm):
    Employer_company_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    Duration = models.CharField(max_length=20)
    Stipend = models.CharField(max_length=5)
    class Meta:
        model = post_job
        fields = ('Employer_company_name','Start_date','Duration','Stipend')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )


#new
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'category', 'Start_date', 'Duration','Stipend','location')

    def __init__(self, user, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location 
        fields = ('name',)  
