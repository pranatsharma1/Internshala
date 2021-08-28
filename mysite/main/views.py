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
            mail_subject = 'Activate your blog account.'
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
            mail_subject = 'Activate your blog account.'
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


#view for homepage of our website
class homepage(View):
    ''' View for homepage of our website '''
    def get(self,request):                                              
        return render(request=request,
                      template_name="main/home.html",
                    )


class student_profile(View):
    ''' View for student profile '''
    def get(self,request):      
        try :  
            student = Student.objects.get(user = request.user)
        except Student.DoesNotExist:
            return redirect("main:homepage")                                        
        return render(request=request,
                      template_name="main/StudentProfile.html",
                      context={"intern":Job.objects.all(), "student" : student}, 
                    )   


class company_profile(View):
    ''' view for company profile '''
    def get(self,request):
        try :      
            company = Company.objects.get(user = request.user)
        except Company.DoesNotExist : 
            return redirect("main:homepage")
        return render(request=request,
                      template_name="main/Employer-Profile.html",
                      context={"jobs":Job.objects.all(), "company" : company},
                    )


class post_a_job(View):
    ''' View for posting the internship '''
    def get(self, request):
        form = Job_Post(request.user)
        categories = Category.objects.all()
        locations = Location.objects.all()
        return render(request = request,
                    template_name = "main/post_job.html",
                    context={"form":form, "categories" : categories, "locations" : locations}) 

    def post(self, request):
        form = Job_Post(request.user, request.POST)
        if form.is_valid():
            job_profile = form.save(commit=False)
            company = Company.objects.get(user = request.user)  
            job_profile.company = company  
            job_profile.save()                
            title = form.cleaned_data.get('job_title')
            messages.success(request, f"New Job created: {title}")   
            
            return redirect("main:company")
        else :
            print(form.errors)
            return redirect("main:company")

@login_required
def internship_detail(request,internship_id):
    ''' View for applying to the internship '''
    job = Job.objects.get(pk = internship_id)
    applicant = Student.objects.get(user = request.user)
    if request.method == 'POST':
        form = Apply_Job(request.POST)
        if form.is_valid():
            apps = Application.objects.filter(intern__user = request.user.id, job = internship_id).count()
            if(apps == 0): 
                application = form.save(commit = False)
                application.intern = Student.objects.get(user = request.user)
                application.job = Job.objects.get(pk = internship_id)
                application.save()
                messages.success(request,"Successfully applied for the Internship")
                return redirect("main:student")
            else : 
                messages.error(request,"You have already applied for this role")
                return redirect("main:student")

    form = Apply_Job()
    return render(request,"main/job_details.html",{'job' : job, 'student' : applicant, "form" : form})


def job_status(request,intern_id):
    ''' View for checking the status of applied internship '''
    intern_id= Intern.objects.get(pk=intern.id)
    return render(request,"main/job_status",{'intern':intern_id,})
        
#-------------------------View for seeing the details of the intern who has applied for the job--------------------------#

@login_required
def application_detail(request, application_id):
    try : 
        applicant = Application.objects.get(id = application_id, job__company__user = request.user.id)
    except Application.DoesNotExist :
        messages.error(request, "No such application exist")
        return redirect("main:company")
    return render(request,"main/intern_details.html",{'applicant' : applicant})

class accept(View):
    ''' View for accepting the Application '''
    def get(self,request, application_id):

        try : 
            application = Application.objects.get(job__company__user = request.user.id, id = application_id)
        except Application.DoesNotExist :
            messages.error(request, "No such application exist")
            return redirect("main:company")
        
        application.is_accept = True
        application.is_reject = False

        subject= 'Application Accepted'
        message='Hello '+ application.intern.user.first_name + " " + application.intern.user.last_name + ', Your application for '+ application.job.job_title +' has been accepted by '+ application.job.company.user.name + "."
        from_email = settings.EMAIL_HOST_USER
        to_email=[application.intern.user.email]
       
        send_mail(subject,message,from_email,to_email,fail_silently=False,)
        application.save()
        
        return redirect("main:company")        

class reject(View):
    ''' View for rejecting the Application '''
    def get(self,request,application_id):

        try : 
            application = Application.objects.get(job__company__user = request.user.id, id = application_id)
        except Application.DoesNotExist :
            messages.error(request, "No such application exist")
            return redirect("main:company")
        application.is_accept = False
        application.is_reject = True

        subject= 'Application Rejected'
        message='Hello '+ application.intern.user.first_name + " " + application.intern.user.last_name + ', Sorry your application for '+ application.job.job_title +' has been rejected by '+ application.job.company.user.name + "."
        from_email = settings.EMAIL_HOST_USER
        to_email=[application.intern.user.email]
       
        send_mail(subject,message,from_email,to_email,fail_silently=False,)
        application.save()

        return redirect("main:company")    

class myapplication(View):
    ''' View for Student to check the status of his application '''
    def get(self,request):
        try :
            application = Application.objects.filter(intern__user = request.user.id)
        except Application.DoesNotExist :
            messages.error(request, "No Applications Found")
            return redirect("main:student")
        return render(request=request,template_name="main/myapplication.html",context={"application" : application})

class interns_applied(View):
    ''' View for the company to see who has applied for the posted internships '''
    def get(self,request):

        try : 
            applicant = Application.objects.filter(job__company__user = request.user.id) 
        except Application.DoesNotExist :
            messages.error(request, "No Applications Found")
            return redirect("main:company")
        return render(request=request, template_name = "main/interns_applied.html",context={"applicant" : applicant})        

class accepted_interns(View):
    ''' View for the company to see the application of accepted interns '''
    def get(self,request):
        application = Application.objects.filter(job__company__user = request.user.id, is_accept = True)
        return render(request=request,template_name="main/accepted_interns.html",context={"application" : application},)

class rejected_interns(View):
    ''' View for the company to see the application of rejected interns '''
    def get(self,request):
        application = Application.objects.filter(job__company__user = request.user.id, is_reject = True)
        return render(request=request,template_name="main/rejected_interns.html",context={"application" : application},)

def delete_internship(request, pk):
    try:
        job = Job.objects.get(company__user = request.user.id, pk = pk)
    except Job.DoesNotExist :
        messages.error(request, "No Internship found")
        return redirect("main:company")

    job.delete()
    messages.success(request, "Successfully deleted the internship")
    return redirect("main:company")

def edit_this_internship(request,pk):
    ''' View for the company to Edit an internship '''
    categories = Category.objects.all()
    locations = Location.objects.all()

    try:
        job = Job.objects.get(company__user = request.user.id, pk = pk)
    except Job.DoesNotExist :
        messages.error(request, "No Internship found")
        return redirect("main:company")

    if request.method=='POST':
        form=EditInternship(request.POST,instance=job)

        if form.is_valid():
            job=form.save()
            messages.success(request,"Internship Edited successfully!!")
            return redirect("main:internship_list")

    else:
        form = EditInternship(instance = job)

    return render(request,"main/edit_this_internship.html",{'form':form,'i':job, "categories" : categories, "locations" : locations})


class logout_request(View):
    def get(self,request):
       logout(request)
       return redirect("main:homepage") 


class login_request(View):
    form_class=AuthenticationForm
    initial={'key':'value'}
    template_name="main/Login-Page.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request=request,data=request.POST)
        if form.is_valid():                                                  
            username = form.cleaned_data.get('username')                     
            password = form.cleaned_data.get('password')                     
            user = authenticate(username=username, password=password)        
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
            username = form.cleaned_data.get('username')                     
            password = form.cleaned_data.get('password')                     
            # user = authenticate(username=username, password=password)
            try:
                user=User.objects.get(username=username)
                if user.is_active is False:
                    messages.error(request,"Verify your Email First")
            except:                                                                    
                messages.error(request, "Invalid username or password.")         
            
            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})


class internship_list(View):
    ''' View for company to display the internships posted '''
    def get(self,request):
        company = Company.objects.get(user = request.user)
        internships = Job.objects.filter(company = company)
        return render(request, 'main/posted_internships.html', {'internships': internships})
                

#--------------------------------------View for Editing the profile of Employer------------------------------------------#

@login_required
def edit_company_profile(request):
    ''' View for the Company to edit profile '''
    if request.method == 'POST':
        form = EditEmployerProfileForm(request.POST,request.FILES or None,instance=request.user)

        if form.is_valid():
            company = Company.objects.get(user = request.user)
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

    else:
        form = EditEmployerProfileForm(instance=request.user)
        company = Company.objects.get(user = request.user)
        args = {'form': form, 'company' : company}
        return render(request, 'main/edit_profile.html', args)

#--------------------------------------View for Editing the profile of Student------------------------------------------#

@login_required
def edit_student_profile(request):
    ''' View for student to edit profile '''
    if request.method == 'POST':
        form = EditStudentProfileForm(request.POST,request.FILES or None, instance=request.user)

        if form.is_valid():
            student = Student.objects.get(user = request.user)
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
    else:
        form = EditStudentProfileForm(instance=request.user)
        student = Student.objects.get(user = request.user)
        args = {'form': form, 'student' : student}
        return render(request, 'main/edit_profile.html', args)

#--------------------------------------View for Changing the password of account------------------------------------------#

@login_required
def change_password(request):
    ''' View to change the password '''
    if request.method == 'POST':
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
            messages.success(request, 'Invaild Details. Re-enter the details !!')
            return redirect(reverse('main:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'main/change_password.html', args)



#-----------------------View to show the filter internship page where the locations and category are seen----------------#
class filter_internship(View):
    ''' View to show the filter internship page where the locations and category are seen '''
    def get(self,request):
        return render(request,
                      template_name="main/Internship_filter.html",
                      context={"filter":Job.objects.all()},
                    )

#----------------------------------------View to show all internships posted----------------------------------------------#
class all_internships(View):
    ''' View to show all the internships posted on Internpedia '''
    def get(self,request):
        return render(request=request,
                      template_name="main/jobs_list.html",
                      context={"jobs":Job.objects.all()},
                    )   

class internships_by_location(View):
    ''' View to show internships based on the location '''
    def get(self, request, location_id):
        d = Job.objects.filter(location = location_id)
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

class internships_by_category(View):
    ''' View to show internships based on the category '''
    def get(self, request, category_id):
        d = Job.objects.filter(category = category_id)
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})    

def pdf_view(request):
    with open('/path/to/my/file.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), contenttype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed
