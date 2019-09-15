
from django.urls import path
from . import views

app_name="main"

urlpatterns = [
   path("",views.homepage,name="homepage"),
   path("student_profile/",views.student_profile,name="student_profile"),
   path("company_profile",views.company_profile,name="company_profile"),

   path("register_as_employer/", views.register_as_employer, name="register_as_employer"), 
   path("register_as_student/", views.register_as_student, name="register_as_student"), 
   path("logout/", views.logout_request, name="logout"), 
   path("login/", views.login_request, name="login"),
   path("student_profile/",views.student,name="student"),
   path("employer_profile/",views.employer,name="employer"),
   path("profile/edit/",views.edit_profile,name="edit_profile"),
   path("change-password/",views.change_password,name="change_password"),
   path('account/', views.view_profile, name='view_profile'),
   path('account/(?P<pk>\d+)/', views.view_profile, name='view_profile_with_pk'),
   path('category/', views.postform, name='postform'),
   path(r'^$', views.HomeView, name='home'),


]
