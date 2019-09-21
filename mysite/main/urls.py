
from django.urls import path
from . import views
from django.conf.urls import url
from main.views import homepage,jobs_in_Delhi,jobs_in_Mumbai,jobs_in_Chennai,jobs_in_Bangalore,student_profile,employer_profile,logout_request,apply_for_job
from main.views import post_a_job,interns_applied,register_as_employer,register_as_student,login_request,web_developer_internship
from main.views import web_developer_internship,android_developer_internship,photographer_internship,video_editor_internship
app_name="main"

urlpatterns = [
   path("",homepage.as_view(),name="homepage"),
   path("register_as_employer/",register_as_employer.as_view(), name="register_as_employer"), 
   path("register_as_student/", register_as_student.as_view(), name="register_as_student"), 
   path("logout/", logout_request.as_view(), name="logout"), 
   path("login/",login_request.as_view(), name="login"),
   path("student_profile/",student_profile.as_view(),name="student"),
   path("jobs_in_Delhi/",jobs_in_Delhi.as_view(),name="jobs_in_Delhi"),
   path("jobs_in_Mumbai/",jobs_in_Mumbai.as_view(),name="jobs_in_Mumbai"),
   path("jobs_in_Chennai/",jobs_in_Chennai.as_view(),name="jobs_in_Chennai"),
   path("jobs_in_Bangalore/",jobs_in_Bangalore.as_view(),name="jobs_in_Bangalore"),
   path("web_developer_internship/",web_developer_internship.as_view(),name="web_developer_internship"),
   path("android_developer_internship/",android_developer_internship.as_view(),name="android_developer_internship"),
   path("video_editor_internship/",video_editor_internship.as_view(),name="video_editor_internship"),
   path("photographer_internship/",photographer_internship.as_view(),name="photographer_internship"),
   path("employer_profile/",employer_profile.as_view(),name="employer"),
   path("post/",post_a_job.as_view(),name="post_a_job"),
   path("apply/",apply_for_job.as_view(),name="apply_for_job"),
   # path("add_location/",add_location.as_view(),name="add_location"),
   # path("add_category/",add_category.as_view(),name="add_category"),
   path("interns_applied/",interns_applied.as_view(),name="interns_applied"),



#    url(r'^$', views.homepage, name='homepage'),
#    url(r'^signup/$', views.register_as_employer, name='register_as_employer'),
#    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         views.activate_account, name='activate'),

]




                                                #Mahima's Code

# <<<<<<< HEAD
   
#    path("login_as_student/", views.login_as_student, name="login_as_student"),
  
# =======
#    path("login/", views.login_request, name="login"), 
#    path("account/",views.account,name="account"),
#    path("add_profile/",views.add_profile,name="add_profile"),

# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d
