from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.



class profile(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=500)
    college = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class postjob(models.Model):
    company_name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Start_date = models.DateField()
    Duration = models.CharField(max_length=10)
    Stipend	 = models.CharField(max_length=10)
    Posted_On = models.DateField(max_length=10)

    def __str__(self):
        return self.company_name

class internship(models.Model):
    company_name = models.CharField(max_length=10,default=None)
    Posted_On = models.DateField(max_length=10,default=None)
    status = models.CharField(max_length=10,default=None)

    def __str__(self):
        return self.company_name



class type_of_field(models.Model):
    name = models.CharField(max_length=10,default=None)
    field = models.ForeignKey(internship,on_delete=models.CASCADE)    

    def __str__(self):
        return self.name

    
class student(models.Model):
    username = models.CharField(max_length=10,default=None)
    Name = models.CharField(max_length=10,default=None)
    College = models.CharField(max_length=10,default=None)
    Skill = models.CharField(max_length=10,default=None)
    phone_no = models.CharField(max_length=10,default=None)
    field = models.CharField(max_length=30,default=None)
    first_n=models.CharField(max_length=40,default=None)
    get_intership = models.ForeignKey(type_of_field,on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Job(models.Model):
    job_title= models.CharField(max_length=200)
    job_content= models.TextField()
    job_published= models.DateTimeField("date published",default= datetime.now())

    def __str__(self):
        return self.job_title
