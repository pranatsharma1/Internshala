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


from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.forms import modelformset_factory
from django.urls import reverse


from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

User=get_user_model()



#-------------------------------------------View for Signup Page of Employer----------------------------------------------#
class register_as_employer(View):
    form_class=NewUserForm1
    initial={'key':'value'}
    template_name="main/Employer-Signup.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST or None,request.FILES or None)
        if form.is_valid():                                                     #if the form filled is valid
            user = form.save()                                           #basically save the user(since user is a part of form,thus we save the form)
            username = form.cleaned_data.get('username')                     #getting the username from the form   
            user.is_active = False
            user.save()
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
        
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})



#-------------------------------------------View for Signup Page of Student----------------------------------------------#

class register_as_student(View):
    form_class=NewUserForm2
    initial={'key':'value'}
    template_name="main/Student-Signup.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST or None,request.FILES or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.is_active = False
            user.save()
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


#-------------------------------------------View for Account Activation--------------------------------------------------#


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


#-------------------------------------------------View for HomePage------------------------------------------------------#


#view for homepage of our website
class homepage(View):
   def get(self,request):                                              
        return render(request=request,
                      template_name="main/home.html",
                    )

#------------------------------------------------View for Student Profile----------------------------------------------#


class student_profile(View):
    def get(self,request):                                                
        return render(request=request,
                      template_name="main/StudentProfile.html",
                      context={"intern":Job.objects.all()}, 
                    )   

#------------------------------------------------View for Student Profile-------------------------------------------------#

class employer_profile(View):
    def get(self,request):                                              
        return render(request=request,
                      template_name="main/Employer-Profile.html",
                      context={"jobs":Job.objects.all()},
                    )

#------------------------------------------------View for Posting the Job-------------------------------------------------#


def post_a_job(request):                                      
    if request.method == "POST":                                                #if user hits the sign up button
        form = Job_Post(request.user,request.POST)                                #mapping the submitted form to user creation form
        if form.is_valid():                                                     #if the form filled is valid
            job_profile = form.save(commit=False)  
            job_profile.user=request.user  
            job_profile.save()                                       #basically save the user(since user is a part of form,thus we save the form)
            title = form.cleaned_data.get('job_title')                     #getting the username from the form   
            messages.success(request, f"New Job created: {title}")    #displaying the message that new account has been created
            
            return redirect("main:employer")
        
    form = Job_Post(request.user)
    return render(request = request,
                  template_name = "main/post_job.html",
                  context={"form":form}) 

#---------------------------------------View for student to apply for an internship-------------------------------------#


def apply_for_job(request):
    if request.method== "POST":
        form = Apply_Job(request.POST)
        if form.is_valid():
            intern_profile= form.save(commit=False)
            
            intern_profile.username=request.user
            intern_profile.save()
            
            messages.success(request,"You have succesully applied for this job")

            return redirect("main:student")
        else:                                                 #if form is not valid or not filled properly               
           
            return render(request = request,
                          template_name = "main/apply_for_job.html",
                          context={"form":form})


    form = Apply_Job()
    return render(request = request,
                  template_name = "main/apply_for_job.html",
                  context={"form":form}) 

#------------------------------------------View for seeing the details of the internship posted---------------------------#

@login_required
def job_detail(request,job_id):
    job_id = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = Apply_Job(request.POST)
        if form.is_valid():
            intern_profile=form.save(commit=False) 
            intern_profile.save()
            messages.success(request,"Successfully applied for the Internship")
            return redirect("main:student")

    form = Apply_Job()
    return render(request,"main/job_details.html",{'j':job_id,"form":form})

#---------------------------------------View for checking the status of applied internship-------------------------------#

def job_status(request,intern_id):
    intern_id= Intern.objects.get(pk=intern.id)
    return render(request,"main/job_status",{'intern':intern_id,})
        
#-------------------------View for seeing the details of the intern who has applied for the job--------------------------#

@login_required
def intern_detail(request,intern_id):
    intern_id = Intern.objects.get(id=intern_id)

    return render(request,"main/intern_details.html",{'intern':intern_id})

class accept(View):

    def get(self,request,intern_id):
        print(intern_id)
        intern=Intern.objects.get(id=intern_id)

        intern.is_accept=True
        intern.is_reject=False

        intern.save()

        return redirect("main:employer")        

class reject(View):

    def get(self,request,intern_id):
        intern=Intern.objects.get(id=intern_id)

        intern.is_accept=False
        intern.is_reject=True

        intern.save()

        return redirect("main:employer")    

#---------------------------------------View for checking the status of applied internship-------------------------------#
class myapplication(View):
    def get(self,request):
       
       i=Intern.objects.filter(username=request.user)

       return render(request=request,template_name="main/myapplication.html",context={"intern":i})



#-----------------------------View for seeing who has applied for your posted intrnship----------------------------------#

class interns_applied(View):

    def get(self,request):

        #only details of those interns are passed to the template 
        #whose comany name equals to the username of the user currently logged in
        i=Intern.objects.filter(company_name=request.user) 
        return render(request=request,template_name="main/jobs_posted.html",context={"intern":i},)

class accepted_interns(View):

    def get(self,request):
        i=Intern.objects.filter(company_name=request.user)
        return render(request=request,template_name="main/accepted_interns.html",context={"intern":i},)

class rejected_interns(View):

    def get(self,request):
        i=Intern.objects.filter(company_name=request.user)
        return render(request=request,template_name="main/rejected_interns.html",context={"intern":i},)


#------------------------------------------View for Editing the Internship-----------------------------------------------#

def edit_this_internship(request,pk):
    job=get_object_or_404(Job,pk=pk)

    if request.method=='POST':
        form=EditInternship(request.POST,instance=job)

        if form.is_valid():
            job=form.save()
            messages.success(request,"Internship Edited successfully!!")
            return redirect("main:internship_list")

    else:
        form = EditInternship(instance = job)

    return render(request,"main/edit_this_internship.html",{'form':form,'i':job})

#----------------------------------View for logging the User out of the current session-----------------------------------#

class logout_request(View):
    def get(self,request):
       logout(request)
    #    messages.info(request, "Logged out successfully!")
       return redirect("main:homepage") 

#----------------------------------View for logging in the user in current session-----------------------------------#

class login_request(View):
    form_class=AuthenticationForm
    initial={'key':'value'}
    template_name="main/Login-Page.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request=request,data=request.POST)
        if form.is_valid():                                                  #if the form is valid
            username = form.cleaned_data.get('username')                     #saving the username form the form
            password = form.cleaned_data.get('password')                     #saving the password from the form
            user = authenticate(username=username, password=password)        #authenticating the user i.e. username and passwords match simultaneously with a user's profile in database
            if user is not None:                                             #basically means "if user is true i.e. if user is successfully authenticated"
                login(request, user)                                         #log the user into the session
                # messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
                if user.is_student:
                  return redirect("main:student")
                else:
                  return redirect("main:employer")                               
            else:                                                            #if it fails to authenticate
                messages.error(request, "Invalid username or password.")     #display an error message
                form=self.form_class(initial=self.initial)
                return render(request ,self.template_name,{'form':form})
        
        else:                                                                #if the form is not valid
            messages.error(request, "Invalid username or password.")         #display the error message
            
            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})



#----------------------------View for company to display the internships posted by the company----------------------------#

class internship_list(View):
    def get(self,request):
        internship = Job.objects.filter(user=request.user)
        return render(request, 'main/posted_internships.html', {'internship': internship})
                

#--------------------------------------View for Editing the profile of Employer------------------------------------------#

@login_required
def edit_employer_profile(request):
    if request.method == 'POST':
        form = EditEmployerProfileForm(request.POST,request.FILES or None,instance=request.user)

        if form.is_valid():
            user=form.save()
            
            if 'image' in request.FILES:                 #Editing the image
                user.image=request.FILES['image']
                user.save

            messages.success(request, 'Profile updated successfully!!')
            if user.is_student:
                return redirect("main:student")
            else:
                return redirect("main:employer")

    else:
        form = EditEmployerProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'main/edit_profile.html', args)

#--------------------------------------View for Editing the profile of Student------------------------------------------#

@login_required
def edit_student_profile(request):
    if request.method == 'POST':
        form = EditStudentProfileForm(request.POST,request.FILES or None, instance=request.user)

        if form.is_valid():
            user=form.save()

            if 'image' in request.FILES:                 #Editing the image
                user.image=request.FILES['image']
                user.save
            
            messages.success(request, 'Profile updated successfully!!')

            if user.is_student:
                return redirect("main:student")
            else:
                return redirect("main:employer")

            
    else:
        form = EditStudentProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'main/edit_profile.html', args)

#--------------------------------------View for Changing the password of account------------------------------------------#

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, 'Password Changed Successfully!!')

            if user.is_student:
                return redirect(reverse('main:student'))
            else:
                return redirect(reverse('main:employer'))

        else:
            messages.success(request, 'Invaild Details. Re-enter the details !!')
            return redirect(reverse('main:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'main/change_password.html', args)



#-----------------------View to show the filter internship page where the locations and category are seen----------------#
class filter_internship(View):
    def get(self,request):
        return render(request,
                      template_name="main/Internship_filter.html",
                      context={"filter":Job.objects.all()},
                    )

#----------------------------------------View to show all internships posted----------------------------------------------#
class all_jobs(View):
    def get(self,request):
        return render(request=request,
                      template_name="main/jobs_list.html",
                      context={"jobs":Job.objects.all()},
                    )   

#-----------------------------------View to display the jobs posted by the company in Delhi-------------------------------#
class jobs_in_Delhi(View):
    def get(self,request):
        d=Job.objects.filter(location='Delhi')
        return render(request=request,
                      template_name="main/jobs_list.html",
                      context={"jobs":d},
                    )   

#----------------------------------View to display the jobs posted by the company in Mumbai-------------------------------#
class jobs_in_Mumbai(View):
    def get(self,request):
        d=Job.objects.filter(location='Mumbai')
        return render(request=request,
                      template_name="main/jobs_list.html",
                      context={"jobs":d},
                    )     

#----------------------------------View to display the jobs posted by the company in Chennai------------------------------#
class jobs_in_Chennai(View):
    def get(self,request):
        d=Job.objects.filter(location='Chennai')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})       



#----------------------------------View to display the jobs posted by the company in Bangalore----------------------------#
class jobs_in_Bangalore(View):
    def get(self,request):
        d=Job.objects.filter(location='Bangalore')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})                

#----------------------------------------View to display the Web Developer Internships-----------------------------------#
class web_developer_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Web Development')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

#--------------------------------------View to display the Android Developer Internships---------------------------------#
class android_developer_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Android Development')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

#--------------------------------------View to display the Photographer Internships---------------------------------------#
class designing_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Designing')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})




def pdf_view(request):
    with open('/path/to/my/file.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), contenttype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed