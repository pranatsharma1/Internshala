from django.contrib import admin
from .models import Job,typeofregister
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class JobAdmin(admin.ModelAdmin):

    fieldsets= [
        ("Title/Date", {"fields": ["job_title","job_published"] }),
        ("Content", {"fields": ["job_content"]}),
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Job,JobAdmin)
admin.site.register(typeofregister)
