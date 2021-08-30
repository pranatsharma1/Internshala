
from django.urls import path
from . import views
from django.conf.urls import url
from main.views import *
app_name="main"

urlpatterns = [
        path("",homepage.as_view(),name="homepage"),
        path("register_as_company/",register_as_company.as_view(), name="register_as_company"), 
        path("register_as_student/", register_as_student.as_view(), name="register_as_student"), 
        path("login/",login_request.as_view(), name="login"),
        path("logout/", logout_request.as_view(), name="logout"), 
        path("company_profile/",company_profile.as_view(),name="company"),
        path("student_profile/",student_profile.as_view(),name="student"),
        path("profile/edit_company/",edit_company_profile.as_view(),name="edit_company_profile"),
        path("profile/edit_student/",edit_student_profile.as_view(),name="edit_student_profile"),
        path("change-password/",change_password.as_view(),name="change_password"),

        path("post_internship/", post_internship.as_view(), name='post_a_job'),
        path("edit_internship/<int:pk>/",views.edit_this_internship,name="edit_this_internship"),
        path("delete_internship/<int:pk>/", views.delete_internship, name = "delete_internship"),
        path('internships_posted/', internships_posted.as_view(), name='internship_list'),
        path("interns_applied/",interns_applied.as_view(),name="interns_applied"),
        path("application_detail/<int:application_id>/",views.application_detail,name="application_detail"),
        path("choose/<int:application_id>/approve/",views.accept.as_view(),name="accept"),
        path("choose/<int:application_id>/reject/",views.reject.as_view(),name="reject"),
        path("accepted_interns/",views.accepted_interns.as_view(),name="accepted_interns"),
        path("rejected_interns/",views.rejected_interns.as_view(),name="rejected_interns"),
        
        path("filter_internship/",filter_internship.as_view(),name="filter_internship"),
        path("all_internships/",all_internships.as_view(),name="all_jobs"),
        path("internships_by_location/<int:location_id>",internships_by_location.as_view(), name = "internships_by_location"),
        path("internships_by_interest/<int:category_id>",internships_by_category.as_view(), name = "internships_by_category"),
        path('myapplication/', myapplication.as_view(), name='myapplication'),
        path("internship_detail/<int:internship_id>/",views.internship_detail,name="internship_detail"),
        
        url(r'^$', views.homepage, name='homepage'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                views.activate, name='activate'),

]
