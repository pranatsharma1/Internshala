
from django.urls import path
from . import views
from django.conf.urls import url
from main.views import *
app_name="main"

urlpatterns = [
   path("",homepage.as_view(),name="homepage"),
   path("register_as_employer/",register_as_employer.as_view(), name="register_as_employer"), 
   path("register_as_student/", register_as_student.as_view(), name="register_as_student"), 
   path("logout/", logout_request.as_view(), name="logout"), 
   path("login/",login_request.as_view(), name="login"),
   path("employer_profile/",employer_profile.as_view(),name="employer"),
   path("student_profile/",student_profile.as_view(),name="student"),

   path("filter_internship/",filter_internship.as_view(),name="filter_internship"),
   
   path("all_jobs/",all_jobs.as_view(),name="all_jobs"),
   path("jobs_in_Delhi/",jobs_in_Delhi.as_view(),name="jobs_in_Delhi"),
   path("jobs_in_Mumbai/",jobs_in_Mumbai.as_view(),name="jobs_in_Mumbai"),
   path("jobs_in_Bangalore/",jobs_in_Bangalore.as_view(),name="jobs_in_Bangalore"),

   path("web_developer_internship/",web_developer_internship.as_view(),name="web_developer_internship"),
   path("android_developer_internship/",android_developer_internship.as_view(),name="android_developer_internship"),
   path("designing_internship/",designing_internship.as_view(),name="designing_internship"),
   
   path("apply/",views.apply_for_job,name="apply_for_job"),

   path("interns_applied/",interns_applied.as_view(),name="interns_applied"),


   path("profile/edit_student/",views.edit_student_profile,name="edit_student_profile"),
   path("profile/edit_employer/",views.edit_employer_profile,name="edit_employer_profile"),
   path("change-password/",views.change_password,name="change_password"),

   path("post_internship/", views.post_a_job, name='post_a_job'),
   path('internship/list/', internship_list.as_view(), name='internship_list'),
   path('myapplication/', myapplication.as_view(), name='myapplication'),
   path("job_detail/<int:job_id>/",views.job_detail,name="job_detail"),
   path("edit_internship/<int:pk>/",views.edit_this_internship,name="edit_this_internship"),
   path("intern_detail/<int:intern_id>/",views.intern_detail,name="intern_detail"),
   path("job_status/<int:intern_id>/",views.job_status,name="job_status"),
   path("choose/<int:intern_id>/approve/",views.accept.as_view(),name="accept"),
   path("choose/<int:intern_id>/reject/",views.reject.as_view(),name="reject"),
   path("accepted_interns/",views.accepted_interns.as_view(),name="accepted_interns"),
   path("rejected_interns/",views.rejected_interns.as_view(),name="rejected_interns"),


   url(r'^$', views.homepage, name='homepage'),
   # url("signup/", views.signup, name='signup'),
   url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
        

]
