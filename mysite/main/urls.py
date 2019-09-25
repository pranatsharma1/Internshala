from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf.urls import url
from main.views import homepage,jobs_in_Delhi,jobs_in_Mumbai,jobs_in_Chennai,jobs_in_Bangalore,student_profile,employer_profile,logout_request
from main.views import post_a_job,interns_applied,register_as_employer,register_as_student,login_request,web_developer_internship
from main.views import filter_internship,web_developer_internship,android_developer_internship,photographer_internship,video_editor_internship
from main.views import post_a_job,internship_list,myapplication
app_name="main"

urlpatterns = [
   path("",homepage.as_view(),name="homepage"),
   path("register_as_employer/",register_as_employer.as_view(), name="register_as_employer"), 
   path("register_as_student/", register_as_student.as_view(), name="register_as_student"), 
   path("logout/", logout_request.as_view(), name="logout"), 
   path("login/",login_request.as_view(), name="login"),
   path("employer_profile/",employer_profile.as_view(),name="employer"),
   path("student_profile/",student_profile.as_view(),name="student"),

   # path("post/",views.post_a_job,name="post_a_job"),

   path("filter_internship/",filter_internship.as_view(),name="filter_internship"),

   path("jobs_in_Delhi/",jobs_in_Delhi.as_view(),name="jobs_in_Delhi"),
   path("jobs_in_Mumbai/",jobs_in_Mumbai.as_view(),name="jobs_in_Mumbai"),
   path("jobs_in_Chennai/",jobs_in_Chennai.as_view(),name="jobs_in_Chennai"),
   path("jobs_in_Bangalore/",jobs_in_Bangalore.as_view(),name="jobs_in_Bangalore"),

   path("web_developer_internship/",web_developer_internship.as_view(),name="web_developer_internship"),
   path("android_developer_internship/",android_developer_internship.as_view(),name="android_developer_internship"),
   path("video_editor_internship/",video_editor_internship.as_view(),name="video_editor_internship"),
   path("photographer_internship/",photographer_internship.as_view(),name="photographer_internship"),
   
   
  # path("apply/",apply_for_job.as_view(),name="apply_for_job"),

   path("interns_applied/",interns_applied.as_view(),name="interns_applied"),


   path("profile/edit/",views.edit_profile,name="edit_profile"),
   path("change-password/",views.change_password,name="change_password"),

   path("post_internship/", views.post_a_job, name='post_a_job'),
   path('internship/edit_all/', views.edit_all_internship, name='edit_all_internship'),
   path('internship/list/', internship_list.as_view(), name='internship_list'),
   path('myapplication/', myapplication.as_view(), name='myapplication'),
   path("job_detail/<int:job_id>/",views.job_detail,name="job_detail"),
   path("job_list/",views.job_list,name="job_list"),

   #path(r'^search/$', views.search, name='search'),


   url(r'^$', views.homepage, name='homepage'),
   # url("signup/", views.signup, name='signup'),
   #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      #  views.activate, name='activate'),
        

]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)