from django.db import models
from datetime import datetime
# Create your models here.
class Job(models.Model):
    job_title= models.CharField(max_length=200)
    job_content= models.TextField()
    job_published= models.DateTimeField("date published",default= datetime.now())

    def __str__(self):
        return self.job_title