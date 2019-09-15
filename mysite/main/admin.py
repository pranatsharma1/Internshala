from django.contrib import admin
from .models import Job
# from .models import Job,profile,skillcategory,postjob,internship
from tinymce.widgets import TinyMCE
from django.db import models
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class JobAdmin(admin.ModelAdmin):

    fieldsets= [
        ("Title/Date", {"fields": ["job_title","job_published"] }),
        ("Stipend",{"fields":["job_stipend"] }),
        ("Content", {"fields": ["job_content"]}),
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(User)                                   #registering the User in Admin
admin.site.register(Job,JobAdmin)                           #registering the Job in Admin



# admin.site.register(skillcategory)
# admin.site.register(profile)
# admin.site.register(postjob)
# admin.site.register(internship)






