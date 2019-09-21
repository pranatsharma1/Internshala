
from django.urls import path
from . import views
from django.conf.urls import url
from main.views import homepage,jobs_list,student_profile,employer_profile,logout_request,add_category,add_location,apply_for_job
from main.views import post_a_job,interns_applied,register_as_employer,register_as_student,login_request
app_name="main"

urlpatterns = [
   path("",homepage.as_view(),name="homepage"),
   path("register_as_employer/",register_as_employer.as_view(), name="register_as_employer"), 
   path("register_as_student/", register_as_student.as_view(), name="register_as_student"), 
   path("logout/", logout_request.as_view(), name="logout"), 
   path("login/",login_request.as_view(), name="login"),
   path("student_profile/",student_profile.as_view(),name="student"),
   path("jobs_list/",jobs_list.as_view(),name="jobs_list"),
   path("employer_profile/",employer_profile.as_view(),name="employer"),
   path("post/",post_a_job.as_view(),name="post_a_job"),
   path("apply/",apply_for_job.as_view(),name="apply_for_job"),
   path("add_location/",add_location.as_view(),name="add_location"),
   path("add_category/",add_category.as_view(),name="add_category"),
   path("interns_applied/",interns_applied.as_view(),name="interns_applied"),
   path("profile/edit/",views.edit_profile,name="edit_profile"),
   path("change-password/",views.change_password,name="change_password"),
 



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
