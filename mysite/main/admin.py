from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import UserProfile,Job,User,post_job,Intershiplocation,IntershipCategory,Products,Category,Location


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'Info'
#new 
   

class JobAdmin(admin.ModelAdmin):

    fieldsets= [
        ("Title/Date", {"fields": ["job_title","job_published"] }),
        ("Content", {"fields": ["job_content"]}),
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(User)
admin.site.register(Job,JobAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(post_job)
admin.site.register(Intershiplocation)
admin.site.register(IntershipCategory)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Products)












