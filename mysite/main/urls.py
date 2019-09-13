
from django.urls import path
from . import views

app_name="main"

urlpatterns = [
   path("",views.homepage,name="homepage"),
   path("register_as_employer/", views.register_as_employer, name="register_as_employer"), 
   path("register_as_student/", views.register_as_student, name="register_as_student"), 
   path("logout/", views.logout_request, name="logout"), 
# <<<<<<< HEAD
   path("login/", views.login_request, name="login"),
#    path("login_as_student/", views.login_as_student, name="login_as_student"),
   path("student_profile/",views.student,name="student"),
   path("employer_profile/",views.employer,name="employer"),
# =======
#    path("login/", views.login_request, name="login"), 
#    path("account/",views.account,name="account"),
#    path("add_profile/",views.add_profile,name="add_profile"),

# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d
]
