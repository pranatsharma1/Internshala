from django.contrib import admin
# from .models import Job, Application,Application_Status, Category, Location
from main.models import *

# from tinymce.widgets import TinyMCE
from django.db import models
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    fieldsets= [
        ("Title/Date", {"fields": ["company", "job_title", "category", "job_published"] }),
        ("Job_Time",{"fields":["location", "job_duration"]}),
        ("Stipend",{"fields":["job_stipend"] }),
        ("Content", {"fields": ["job_content"]}),
    ]

admin.site.register(User)                                   #registering the User in Admin
admin.site.register(Application)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Job, JobAdmin)                           #registering the Job in Admin
admin.site.register(Company)
admin.site.register(Student)
