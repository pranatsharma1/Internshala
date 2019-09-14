from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    london = UserProfileManager()

    def __str__(self):
        return self.user.username
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                     

