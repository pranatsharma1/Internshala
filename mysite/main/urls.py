
from django.urls import path
from . import views
from django.conf.urls import url

app_name="main"

urlpatterns = [
   path("",views.homepage,name="homepage"),
   path("register_as_employer/", views.register_as_employer, name="register_as_employer"), 
   path("register_as_student/", views.register_as_student, name="register_as_student"), 
   path("logout/", views.logout_request, name="logout"), 
   path("login/", views.login_request, name="login"),
   path("student_profile/",views.student,name="student"),
   path("jobs_list/",views.jobs_list,name="jobs_list"),
   path("employer_profile/",views.employer,name="employer"),
   path("post/",views.post_a_job,name="post_a_job"),
   path("apply/",views.apply_for_job,name="apply_for_job"),
   path("add_location/",views.add_location,name="add_location"),
   path("add_category/",views.add_category,name="add_category"),
   path("interns_applied/",views.interns_applied,name="interns_applied"),
   path('internship/post_a_job/', views.post_a_job, name='post_a_job'),
   path('internship/edit_all/', views.edit_all_internship, name='edit_all_internship'),
   path('internship/list/', views.internship_list, name='internship_list'),
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
