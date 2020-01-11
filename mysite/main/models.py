#A model is the single, definitive source of information about your data. 
#It contains the essential fields and behaviors of the data you’re storing. 
#Generally, each model maps to a single database table.


from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

#user model for Employer and Student
class User(AbstractUser):      
    is_employer=models.BooleanField(default=False)                      #a boolean field to check whether the registered user is employer?
    is_student=models.BooleanField(default=False)                       #a boolean field to check whether the registered user is student?
    image=models.ImageField(upload_to='pics',default="")

    # extra fields for student
    college_name=models.CharField(max_length=200,default="")
    basic_skills=models.TextField(default="")
    city=models.CharField(max_length=200,default="")
    year_of_study=models.IntegerField(choices=((1,"first_year"),(2,"second_year"),(3,"third_year"),(4,"fourth_year")),default=1)



class category(models.Model):
    CHOICES=[
        ('Web Development','Web Development'),
        ('Android Development','Android Development'),
        ('Designing','Designing'),
        ('Photography','Photography'),
        ('Video Editing','Video Editing')
    ]
    category_name=models.CharField(max_length=2,choices=CHOICES,)



# model for Job
class Job(models.Model): 

    Category_Choices=[
        ('Web Development','Web Development'),
        ('Android Development','Android Development'),
        ('Designing','Designing'),
        ('Photography','Photography'),
        ('Video Editing','Video Editing')
    ]
    
    Location_Choices=[
        ('Delhi','Delhi'),
        ('Bangalore','Bangalore'),
        ('Chennai','Chennai'),
        ('Mumbai','Mumbai'),
        ('Ghaziabad','Ghaziabad'),
    ]

    job_title= models.CharField(max_length=200)                     #field: Title of Job. Ex: Front End Developer etc.
    category=models.CharField(max_length=200,choices=Category_Choices,default="")            #Category of Job. Ex: Web Development,Android Development
    location=models.CharField(max_length=200,choices=Location_Choices,default="")            #location of Job. Ex: Delhi,Mumbai,Bangalore,etc.
    job_duration=models.IntegerField(default=1)                                        #field1: Job Title
    job_content= models.TextField()                                                      #field2: Job Content
    job_published= models.DateTimeField("date published",default= datetime.now())        #Date and time of Job Published
    job_stipend=models.IntegerField(default=0)                                         #Stipend of Job
    user=models.ForeignKey(User,default=2,on_delete=models.SET_DEFAULT,null=True)    #Username of Company who has posted the job
    

                        #https://www.quora.com/What-does-def-str__-self-method-does-in-Django

    def __str__(self):              #__str__(self): is used to define how you want to provide string output of your class.
        return self.job_title       #display the job title as heading for the objects of Job model


class Intern(models.Model):
    intern_name=models.CharField(max_length=200,default="")  
    hire =models.CharField(max_length=200,default="")  
    available =models.BooleanField(default=False)
    college_name=models.CharField(max_length=200,default="")
    basic_skills=models.TextField(default="")
    city=models.CharField(max_length=200,default="")
    year_of_study=models.IntegerField(choices=((1,"first_year"),(2,"second_year"),(3,"third_year"),(4,"fourth_year")),default=1)


    username=models.ForeignKey(User,default=2,on_delete=models.SET_DEFAULT,null=True)

    job_title=models.CharField(max_length=200,default="")    
    job_id=models.CharField(max_length=100,default="")
    company_name=models.CharField(max_length=100,default="")
    document = models.FileField(upload_to='documents/')
    phone_no=models.CharField(max_length=10)
    is_accept=models.BooleanField(default=False)
    is_reject=models.BooleanField(default=False)  
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.intern_name                                        

class JobStatus(models.Model):
    is_accept=models.BooleanField(default=False)
    is_reject=models.BooleanField(default=False)
    intern_name=models.CharField(max_length=200,default="")                    
    company_name=models.CharField(max_length=100,default="")                                             
    hire =models.CharField(max_length=200,default="")  
    available =models.CharField(max_length=200,default="")                                         
    job_title=models.CharField(max_length=200,default="")                                                                                  
                                             
    def __str__(self):
        return self.intern_name                                         
    