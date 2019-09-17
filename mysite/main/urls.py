
from django.urls import path
from . import views
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
   path("category/list/", views.list_of_category, name="list_of_category"), 

   #new code
   path('products/all/pro/', views.Studentprofile, name='Studentprofile'),
   #path('products/all/all/', views.Products, name='Products'),

   path('products/new/new/', views.new_product, name='new_product'),
   path('products/edit_all/pro/', views.edit_all_products, name='edit_all_products'),
   path('products/pro/pro/', views.products_list, name='products_list'),
   path('products/categories/new/', views.new_category, name='new_category'),
   path('products/location/new/', views.new_Location, name='new_location'),
   path('products/student/new/', views.student_apply, name='student_apply'),


   #path('internship/new/new/', views.new_internship, name='new_internship'),
   #path('internship/edit_all/pro/', views.edit_all_internship, name='edit_all_internship'),
   #path('internship/pro/pro/', views.internship_list, name='internship_list'),
   #path('internship/categories/new/', views.internship_new_category, name='internship_new_category'),


]
