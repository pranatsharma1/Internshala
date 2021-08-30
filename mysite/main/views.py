#A view function, or “view” for short, is simply a Python function that takes a web request 
#and returns a web response. This response can be the HTML contents of a Web page, or a redirect,
#or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, 
#note that you need to associate a view to a URL to see it as a web page.

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.forms import modelformset_factory
from django.urls import reverse


from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

User=get_user_model()




########################################################### Authentication ###########################################################

class register_as_company(View):
    ''' This view is used for regisitering the company '''
    
    form_class = CompanySignUpForm
    initial={'key':'value'}
    template_name="main/Employer-Signup.html"
    
    def get(self,request):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST or None,request.FILES or None)
        # for field in form:
        #     print("Field Error:", field.name,  field.errors)
        if form.is_valid():      
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(email, password)

            user.active = False
            user.name = form.cleaned_data.get('name')
            user.is_company = True
            user.save()

            company = Company.objects.create(user = user)
            company.save()
            
            current_site = get_current_site(request)
            mail_subject = 'Verify your email to activate your account.'
            message = render_to_string('main/acc_active_email.html', {
                   'user': user,
                   'domain': current_site.domain,
                   'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                   'token': account_activation_token.make_token(user),
                })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return HttpResponse('Please confirm your email address to complete the registration') 

        else:      
            print("ERROR")                                                         
            # for msg in form.error_messages:                   
            #     print(msg)
            #     messages.error(request, f"{msg}: {form.error_messages[msg]}")  
            for field, items in form.errors.items():
                for item in items:
                    print(field)
                    print(item)
                    messages.error(request, f"{field}: {item}")

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})


class register_as_student(View):
    ''' This view is for registering the student '''
    form_class=StudentSignUpForm
    initial={'key':'value'}
    template_name="main/Student-Signup.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST or None,request.FILES or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(email, password)
        
            user.active = False
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.is_student = True
            user.save()

            student = Student.objects.create(user = user)
            student.save()

            current_site = get_current_site(request)
            mail_subject = 'Verify your email to activate your account.'
            message = render_to_string('main/acc_active_email.html', {
                   'user': user,
                   'domain': current_site.domain,
                   'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                   'token': account_activation_token.make_token(user),
                })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration') 
            
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})


def activate(request, uidb64, token):
    ''' View for activating the user after email verification '''
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.active = True
        user.save()
        login(request, user)

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class login_request(View):
    form_class = AuthenticationForm
    initial={'key':'value'}
    template_name="main/Login-Page.html"
    
    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request=request,data=request.POST)
        if form.is_valid():                                                  
            email = form.cleaned_data.get('username')                     
            password = form.cleaned_data.get('password')    
            user = authenticate(email = email, password = password)
            
            if user is not None:
                login(request, user)                                         
                
                if user.is_student:
                  return redirect("main:student")
                else:
                  return redirect("main:company")                               
            else:                                                            
                messages.error(request, "Invalid username or password.")     
                form=self.form_class(initial=self.initial)
                return render(request ,self.template_name,{'form':form})

        else:
            email = form.cleaned_data.get('username')                     
            password = form.cleaned_data.get('password')                     
            user = authenticate(email = email, password=password)
            
            try:
                user=User.objects.get(email = email)
                if user.is_active is False:
                    current_site = get_current_site(request)
                    mail_subject = 'Verify your email to activate your account.'
                    message = render_to_string('main/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                        })
                    to_email = form.cleaned_data.get('email')
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return HttpResponse("Verify your Email first")
            except:                                                                    
                messages.error(request, "Invalid username or password.")         
            
            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})


class logout_request(View):
    def get(self,request):
        logout(request)
        return redirect("main:homepage") 


class change_password(View):
    ''' View to change the password '''
    def get(self, request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        try :
            form = PasswordChangeForm(user=request.user)
        except:
            return redirect("main:homepage")
        args = {'form': form}
        return render(request, 'main/change_password.html', args)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, 'Password Changed Successfully!!')

            if user.is_student:
                return redirect(reverse('main:student'))
            else:
                return redirect(reverse('main:company'))

        else:
            messages.error(request, 'Invaild Details. Re-enter the details !!')
            return redirect(reverse('main:change_password'))


#view for homepage of our website
class homepage(View):
    ''' View for homepage of our website '''
    def get(self,request):                                              
        return render(request=request, template_name="main/home.html")


########################################################### Company Profile ###########################################################

class company_profile(View):
    ''' view for company profile '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        
        try :      
            company = Company.objects.get(user = request.user)
        except Company.DoesNotExist :
            if request.user.is_student :
                messages.error(request, "Access Denied")
                return redirect("main:student") 
            return redirect("main:homepage")

        return render(request=request, template_name="main/Employer-Profile.html", context={"jobs":Internship.objects.all(), "company" : company})


class edit_company_profile(View):
    ''' View for the Company to edit profile '''
    def get(self, request):
        if request.user.is_anonymous:
            return redirect("main:homepage")

        form = EditEmployerProfileForm(instance=request.user)
        try :
            company = Company.objects.get(user = request.user)
        except Company.DoesNotExist:
            if request.user.is_student:
                return redirect("main:edit_student_profile")
            return redirect("main:homepage")

        args = {'form': form, 'company' : company}
        return render(request, 'main/edit_profile.html', args)

    def post(self, request):
        form = EditEmployerProfileForm(request.POST,request.FILES or None,instance=request.user)

        if form.is_valid():
            try :
                company = Company.objects.get(user = request.user)
            except Company.DoesNotExist:
                if request.user.is_student:
                    return redirect("main:edit_student_profile")
                return redirect("main:homepage")

            city = form.cleaned_data.get('head_office_location')
            company.head_office_location = city
            company.save()
            user=form.save()
            
            if 'image' in request.FILES:  
                company.image = request.FILES['image']
                company.save()

            messages.success(request, 'Profile updated successfully!!')
            if user.is_student:
                return redirect("main:student")
            else:
                return redirect("main:company")


class post_internship(View):
    ''' View for posting the internship '''
    def get(self, request):
        if request.user.is_anonymous:
            return redirect("main:homepage")

        if request.user.is_student:
            messages.error(request, "Access Denied")
            return redirect("main:student")

        form = Internship_Post(request.user)
        categories = Category.objects.all()
        locations = Location.objects.all()
        return render(request = request, template_name = "main/post_job.html", context={"form":form, "categories" : categories, "locations" : locations}) 

    def post(self, request):
        form = Internship_Post(request.user, request.POST)
        if form.is_valid():
            job_profile = form.save(commit=False)
            company = Company.objects.get(user = request.user)  
            job_profile.company = company  
            job_profile.save()                
            title = form.cleaned_data.get('role')
            messages.success(request, f"New Internship posted : {title}")   
            return redirect("main:company")
        else :
            print(form.errors)
            return redirect("main:company")


def edit_this_internship(request, pk):
    ''' View for the company to Edit an internship '''
    categories = Category.objects.all()
    locations = Location.objects.all()

    if request.user.is_anonymous:
            return redirect("main:homepage")

    try:
        job = Internship.objects.get(company__user = request.user.id, pk = pk)
    except Internship.DoesNotExist :
        messages.error(request, "Access Denied")
        if request.user.is_company :
            return redirect("main:internship_list")
        else :
            return redirect("main:student")

    if request.method=='POST':
        form=EditInternship(request.POST,instance=job)
        if form.is_valid():
            job=form.save()
            messages.success(request,"Internship Edited successfully!!")
            return redirect("main:internship_list")

    else:
        form = EditInternship(instance = job)

    return render(request,"main/edit_this_internship.html",{'form':form,'i':job, "categories" : categories, "locations" : locations})


def delete_internship(request, pk):
    if request.user.is_anonymous:
            return redirect("main:homepage")
    if request.user.is_student:
            messages.error(request, "Access Denied")
            return redirect("main:student")
    try:
        internship = Internship.objects.get(company__user = request.user.id, pk = pk)
    except Internship.DoesNotExist :
        messages.error(request, "No Internship found")
        return redirect("main:internships_posted")

    internship.delete()
    messages.success(request, "Successfully deleted the internship")
    return redirect("main:company")

class internships_posted(View):
    ''' View for company to display the internships posted '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        if request.user.is_student:
                messages.error(request, "Access Denied")
                return redirect("main:student")
        
        try :
            company = Company.objects.get(user = request.user)
        except Company.DoesNotExist :
            return redirect("main:homepage")
        internships = Internship.objects.filter(company = company)
        return render(request, 'main/posted_internships.html', {'internships': internships})


class interns_applied(View):
    ''' View for the company to see the list of applicants for the posted internships '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        if request.user.is_student:
                messages.error(request, "Access Denied")
                return redirect("main:student")
        try : 
            applicant = Application.objects.filter(internship__company__user = request.user.id) 
        except Application.DoesNotExist :
            messages.error(request, "No Applications Found")
            return redirect("main:company")
        return render(request=request, template_name = "main/interns_applied.html",context={"applicant" : applicant})        


def application_detail(request, application_id):
    ''' View for the company to see the details of a particular application'''
    if request.user.is_anonymous:
            return redirect("main:homepage")
    if request.user.is_student:
        messages.error(request, "Access Denied")
        return redirect("main:student")
    
    try : 
        applicant = Application.objects.get(id = application_id, internship__company__user = request.user.id)
    except Application.DoesNotExist :
        messages.error(request, "No such application exist")
        return redirect("main:company")
    return render(request,"main/intern_details.html",{'applicant' : applicant})


class accept(View):
    ''' View for accepting the Application '''
    def get(self,request, application_id):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        if request.user.is_student:
            messages.error(request, "Access Denied")
            return redirect("main:student")
        
        try : 
            application = Application.objects.get(internship__company__user = request.user.id, id = application_id)
        except Application.DoesNotExist :
            messages.error(request, "No such application exist")
            return redirect("main:company")
        
        application.is_accept = True
        application.is_reject = False

        subject= 'Application Accepted'
        message='Hello '+ application.student.user.first_name + " " + application.student.user.last_name + ', Your application for '+ application.internship.role +' role has been accepted by '+ application.internship.company.user.name + "."
        from_email = settings.EMAIL_HOST_USER
        to_email=[application.student.user.email]
       
        send_mail(subject,message,from_email,to_email,fail_silently=False,)
        application.save()
        
        return redirect("main:company")        


class reject(View):
    ''' View for rejecting the Application '''
    def get(self,request,application_id):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        if request.user.is_student:
            messages.error(request, "Access Denied")
            return redirect("main:student")

        try : 
            application = Application.objects.get(internship__company__user = request.user.id, id = application_id)
        except Application.DoesNotExist :
            messages.error(request, "No such application exist")
            return redirect("main:company")
        application.is_accept = False
        application.is_reject = True

        subject= 'Application Rejected'
        message='Hello '+ application.student.user.first_name + " " + application.student.user.last_name + ', Sorry your application for '+ application.internship.role +' role has been rejected by '+ application.internship.company.user.name + "."
        from_email = settings.EMAIL_HOST_USER
        to_email=[application.student.user.email]

        send_mail(subject,message,from_email,to_email,fail_silently=False,)
        application.save()

        return redirect("main:company")    


class accepted_interns(View):
    ''' View for the company to see the application of accepted interns '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        if request.user.is_student:
            messages.error(request, "Access Denied")
            return redirect("main:student")

        application = Application.objects.filter(internship__company__user = request.user.id, is_accept = True)
        return render(request=request,template_name="main/accepted_interns.html",context={"application" : application},)

class rejected_interns(View):
    ''' View for the company to see the application of rejected interns '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        if request.user.is_student:
            messages.error(request, "Access Denied")
            return redirect("main:student")

        application = Application.objects.filter(internship__company__user = request.user.id, is_reject = True)
        return render(request=request,template_name="main/rejected_interns.html",context={"application" : application},)





########################################################### Student Profile ###########################################################

class student_profile(View):
    ''' View for student profile '''
    def get(self,request):  
        if request.user.is_anonymous:
            return redirect("main:homepage")    
        try :  
            student = Student.objects.get(user = request.user)
        except Student.DoesNotExist:
            return redirect("main:homepage")                                        
        return render(request=request, template_name="main/StudentProfile.html", context={"intern":Internship.objects.all(), "student" : student})   


class edit_student_profile(View):
    ''' View for student to edit profile '''
    def get(self, request):
        if request.user.is_anonymous:
            return redirect("main:homepage")
        form = EditStudentProfileForm(instance=request.user)
        
        try :
            student = Student.objects.get(user = request.user)
        except Student.DoesNotExist:
            if request.user.is_company : 
                return redirect("main:edit_company_profile")
            return redirect("main:homepage")
        args = {'form': form, 'student' : student}
        return render(request, 'main/edit_profile.html', args)

    def post(self, request):
        form = EditStudentProfileForm(request.POST,request.FILES or None, instance=request.user)

        if form.is_valid():
            try :
                student = Student.objects.get(user = request.user)
            except Student.DoesNotExist:
                if request.user.is_company : 
                    return redirect("main:edit_company_profile")
                return redirect("main:homepage")

            student.phone_no = form.cleaned_data.get('phone_no')
            student.college_name = form.cleaned_data.get('college_name')
            student.basic_skills = form.cleaned_data.get('basic_skills')
            student.city = form.cleaned_data.get('city')
            student.year_of_study = form.cleaned_data.get('year_of_study')
            student.save()
            user = form.save()

            if 'image' in request.FILES:   
                print("IMAGE")              
                student.image=request.FILES['image']
                print(student.image)
                student.save()
            
            messages.success(request, 'Profile updated successfully!!')

            if user.is_student:
                return redirect("main:student")
            else:
                return redirect("main:company")


def internship_detail(request,internship_id):
    ''' View for applying to the internship '''
    if request.user.is_anonymous:
            return redirect("main:homepage")

    if request.user.is_company : 
        messages.error(request, "Access Denied")
        return redirect("main:company")

    internship = Internship.objects.get(pk = internship_id)
    applicant = Student.objects.get(user = request.user)
    if request.method == 'POST':
        form = Apply_Internship(request.POST, request.FILES or None)
        if form.is_valid():
            apps = Application.objects.filter(student__user = request.user.id, internship = internship_id).count()
            if(apps == 0): 
                application = form.save(commit = False)
                application.student = Student.objects.get(user = request.user)
                application.internship = Internship.objects.get(pk = internship_id)
                application.save()

                if "resume" in request.FILES:
                    applicant.resume = request.FILES['resume']
                    applicant.save()

                messages.success(request,"Successfully applied for the Internship")
                return redirect("main:student")
            else : 
                messages.error(request,"You have already applied for this role")
                return redirect("main:student")

    form = Apply_Internship()
    return render(request,"main/job_details.html",{'internship' : internship, 'student' : applicant, "form" : form})


class filter_internship(View):
    ''' View to show the filter internship page where the locations and category are seen '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")

        if request.user.is_company :
            messages.error(request, "Access Denied")
            return redirect("main:company")
        return render(request, template_name="main/Internship_filter.html", context={"filter":Internship.objects.all()},)


class all_internships(View):
    ''' View to show all the internships posted on Internpedia '''
    def get(self,request):
        if request.user.is_anonymous is False and request.user.is_company:
            messages.error(request, "Access Denied")
            return redirect("main:company")
        return render(request=request,
                      template_name="main/jobs_list.html",
                      context={"jobs":Internship.objects.all()},
                    )   

class internships_by_location(View):
    ''' View to show internships based on the location '''
    def get(self, request, location_id):
        if request.user.is_anonymous is False and request.user.is_company:
            messages.error(request, "Access Denied")
            return redirect("main:company")
        d = Internship.objects.filter(location = location_id)
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

class internships_by_category(View):
    ''' View to show internships based on the category '''
    def get(self, request, category_id):
        if request.user.is_anonymous is False and request.user.is_company:
            messages.error(request, "Access Denied")
            return redirect("main:company")
        d = Internship.objects.filter(category = category_id)
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})    

class myapplication(View):
    ''' View for Student to check the status of his application '''
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("main:homepage")

        if request.user.is_company : 
            messages.error(request, "Access Denied")
            return redirect("main:company")

        try :
            application = Application.objects.filter(student__user = request.user.id)
        except Application.DoesNotExist :
            messages.error(request, "No Applications Found")
            return redirect("main:student")
        return render(request=request,template_name="main/myapplication.html",context={"application" : application})
