from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

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

