
from django.urls import path
from . import views
from .views import HomeView
from django.conf.urls import url

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
   path('home/', HomeView.as_view()),
   #new code
   url('products/new/new/', views.new_product, name='new_product'),
   url('products/edit_all/pro/', views.edit_all_products, name='edit_all_products'),
   url('products/pro/pro/', views.products_list, name='products_list'),
   url('products/categories/new/', views.new_category, name='new_category'),


]
