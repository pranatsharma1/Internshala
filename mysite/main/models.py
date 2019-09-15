from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm



# Create your models here.

class User(AbstractUser):
    is_employer=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

class Job(models.Model):
    job_title= models.CharField(max_length=200)
    job_content= models.TextField()
    job_published= models.DateTimeField("date published",default= datetime.now())

    def __str__(self):
        return self.job_title 
#new
class IntershipCategory(models.Model):
    intership_category = models.CharField(max_length=200)
    intership_summray = models.CharField(max_length=200)
    
    def __str__(self):
        return self.intership_category


class Intershiplocation(models.Model):
    intership_location = models.CharField(max_length=20)
    intership_category = models.ForeignKey(IntershipCategory,default='',blank=True , null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.intership_location



class post_job(models.Model):
    Employer_company_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    Duration = models.CharField(max_length=20)
    Stipend = models.CharField(max_length=5)
    category = models.ForeignKey(Intershiplocation,default='',blank=True , null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.Employer_company_name


#new above


class UserProfileManager(models.Manager):     #this is for managing the data like filter here make it in function
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100, default='')
    company_location = models.CharField(max_length=100, default='')
    #new
    fieldname_type = models.ForeignKey(post_job,default='',blank=True , null=True,on_delete=models.CASCADE)
    


    london = UserProfileManager()   #userprofile.london.all() same as it 

    def __str__(self):
        return self.user.username
class UserProfileManagerE(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(company_location='delhi')

'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
                                             
class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)                                             
    def __str__(self):
        return self.name                               
                                             
                    