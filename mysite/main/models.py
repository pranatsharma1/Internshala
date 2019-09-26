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
    year_of_study=models.CharField(max_length=200,default="")
                            


# model for Job
class Job(models.Model):      
    job_title= models.CharField(max_length=200)                     #field: Title of Job. Ex: Front End Developer etc.
    category=models.CharField(max_length=200,default="")            #Category of Job. Ex: Web Development,Android Development
    location=models.CharField(max_length=200,default="")            #location of Job. Ex: Delhi,Mumbai,Bangalore,etc.
    job_duration=models.CharField(max_length=200)                                        #field1: Job Title
    job_content= models.TextField()                                                      #field2: Job Content
    job_published= models.DateTimeField("date published",default= datetime.now())        #Date and time of Job Published
    job_stipend=models.CharField(max_length=200)                                         #Stipend of Job
    user=models.ForeignKey(User,default=2,on_delete=models.SET_DEFAULT,null=True)    #Username of Company who has posted the job
    

                        #https://www.quora.com/What-does-def-str__-self-method-does-in-Django

    def __str__(self):              #__str__(self): is used to define how you want to provide string output of your class.
        return self.job_title       #display the job title as heading for the objects of Job model

class Intern(models.Model):
    intern_name=models.CharField(max_length=200,default="")  
    hire =models.CharField(max_length=200,default="")  
    available =models.CharField(max_length=200,default="")   
    username=models.ForeignKey(User,default=2,on_delete=models.SET_DEFAULT,null=True)      
    job_title=models.CharField(max_length=200,default="")    
    job_id=models.CharField(max_length=100,default="")
    company_name=models.CharField(max_length=100,default="")
    document = models.FileField(upload_to='documents/')
    phone_no=models.CharField(max_length=10)
    is_accept=models.BooleanField(default=False)
    is_reject=models.BooleanField(default=False)  

    def __str__(self):
        return self.intern_name                                        
                                             
            
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                              # Mahima's Code

# =======
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from django.core import validators
# from django.utils import timezone


# # Create your models here.
# '''class typeofregister(models.Model):
#     name= models.CharField(max_length=50)
#     type_register = models.CharField(max_length=10)
# '''
# class skillcategory(models.Model):
#     profile_s = models.CharField(max_length=100)
#     Organization = models.CharField(max_length=100)
#     location_s = models.CharField(max_length=100)
#     start_date = models.DateField()
#     last_date = models.DateField()
#     Description = models.CharField(max_length=400)

#     def __str__(self):
#         return self.profile_s



# class profile(models.Model):
#     name = models.CharField(max_length=100)
#     skill = models.CharField(max_length=500)
#     college = models.CharField(max_length=100)
#     phone_no = models.CharField(max_length=10)
#     location = models.CharField(max_length=100)
#     company_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class internship(models.Model):
#     field = models.ForeignKey(profile,on_delete=models.CASCADE)        


# class postjob(models.Model):
#     company_name = models.CharField(max_length=100)
#     about = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     Start_date = models.DateField()
#     Duration = models.CharField(max_length=10)
#     Stipend	 = models.CharField(max_length=10)
#     Posted_On = models.DateField(max_length=10)







# '''

# TITLE_CHOICES = [
#     ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# ]

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3, choices=TITLE_CHOICES)
#     birth_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']

# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']

# '''
# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d


# <<<<<<< HEAD

# =======
# '''
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user      
#     def create_studentuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.student = True
#         user.save(using=self._db)
#         return user
#     def create_companyuser(self, email, password):
#         """
        
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.student = False
#         user.company = True
#         user.save(using=self._db)
#         return user
        

# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     active = models.BooleanField(default=True)
#     student = models.BooleanField(default=False) # a admin user; non super-user
#     company = models.BooleanField(default=False) # a superuser
#     # notice the absence of a "Password field", that's built in.

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # Email & Password are required by default.
 
#     objects = UserManager()

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __str__(self):              # __unicode__ on Python 2
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_student(self):
#         "Is the user a member of staff?"
#         return self.student

#     @property
#     def is_company(self):
#         "Is the user a admin member?"
#         return self.company

#     @property
#     def is_active(self):
#         "Is the user active?"
#         return self.active'''
# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d
