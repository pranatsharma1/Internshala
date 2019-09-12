from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from . models import profile,skillcategory
from django.db import models


class profileform(ModelForm):
    class Meta :
        model = profile
        fields = ("name","skill","college","phone_no","location","company_name")



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    #differ_id = forms.CharField(required=True, label="Differ_Id")


    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user    


