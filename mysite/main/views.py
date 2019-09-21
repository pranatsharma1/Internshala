#A view function, or “view” for short, is simply a Python function that takes a web request 
#and returns a web response. This response can be the HTML contents of a Web page, or a redirect,
#or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, 
#note that you need to associate a view to a URL to see it as a web page.

from django.views import View
from django.shortcuts import render, redirect
from .models import Job,Intern
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import Job_Post,Apply_Job
from .forms import NewUserForm1
from .forms import NewUserForm2

from django.contrib.auth.decorators import login_required



#view for homepage of our website
class homepage(View):
   def get(self,request):                                              
        return render(request=request,template_name="main/home.html",)

#view for student's profile
class student_profile(View):
    def get(self,request):                                                
        return render(request=request,template_name="main/StudentProfile.html",context={"intern":Job.objects.all()} )   


#view for employer's profile
class employer_profile(View):
    def get(self,request):                                              
        return render(request=request,template_name="main/Employer-Profile.html",context={"jobs":Job.objects.all()})

#view to display the details of interns applied for the internship
class interns_applied(View):
    def get(self,request):
        return render(request=request,template_name="main/jobs_posted.html",context={"intern":Intern.objects.all()})

#view to display the jobs posted by the company
class jobs_in_Delhi(View):
    def get(self,request):
        d=Job.objects.filter(location='Delhi')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})   

#view to display the jobs posted by the company
class jobs_in_Mumbai(View):
    def get(self,request):
        d=Job.objects.filter(location='Mumbai')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})     

#view to display the jobs posted by the company
class jobs_in_Chennai(View):
    def get(self,request):
        d=Job.objects.filter(location='Chennai')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})       

#view to display the jobs posted by the company
class jobs_in_Bangalore(View):
    def get(self,request):
        d=Job.objects.filter(location='Bangalore')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})                


class web_developer_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Web Development')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

class android_developer_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Android Development')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

class photographer_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Photography')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})

class video_editor_internship(View):
    def get(self,request):
        d=Job.objects.filter(category='Video Editing')
        return render(request=request,template_name="main/jobs_list.html",context={"jobs":d})                        
# view for adding category
# class add_category(View):
#     form_class=Category
#     initial={'key':'value'}
#     template_name="main/category.html"

#     def get(self,request):
#         form=self.form_class(initial=self.initial)
#         return render(request,self.template_name,{'form':form})

#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#            cat= form.save(commit=False)
#            cat.save()
#            username = form.cleaned_data.get('category')                     #getting the username from the form   
#            messages.success(request, f"New Category {username} created")
#            return redirect("main:employer")   

#         else:                                                 #if form is not valid or not filled properly               
#             for msg in form.error_messages:                   
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages
#             form=self.form_class(initial=self.initial)
#             return render(request ,self.template_name,{'form':form})



# view for adding location
# class add_location(View):
#     form_class=Location
#     initial={'key':'value'}
#     template_name="main/location.html"
    
#     def get(self,request):
#         form=self.form_class(initial=self.initial)
#         return render(request,self.template_name,{'form':form})

#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#            loc= form.save(commit=False)
#            loc.save()
#            username = form.cleaned_data.get('location')                     #getting the username from the form   
#            messages.success(request, f"New Location {username} created")
#            return redirect("main:employer")
#         else:
#             for msg in form.error_messages:                   
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

#             form=self.form_class(initial=self.initial)
#             return render(request ,self.template_name,{'form':form})



# view for applying for job 
class apply_for_job(View):
    form_class=Apply_Job
    initial={'key':'value'}
    template_name="main/apply_for_job.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            intern_profile= form.save(commit=False)
            
            intern_profile.username=request.user
            intern_profile.save()
            #username = form.cleaned_data.get('intern_profile.username')                     #getting the username from the form   
            messages.success(request, f"{intern_profile.username} has succesully applied for this job")

            return redirect("main:student")
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})


# view for posting a job
class post_a_job(View):
    form_class=Job_Post
    initial={'key':'value'}
    template_name="main/post_job.html"

    def get(self,request):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():                                                     #if the form filled is valid
            job_profile = form.save(commit=False)  
            job_profile.username=request.user  
            job_profile.save()                                       #basically save the user(since user is a part of form,thus we save the form)
            username = form.cleaned_data.get('job_title')                     #getting the username from the form   
            messages.success(request, f"New Job created: {username}")    #displaying the message that new account has been created
            
            # now after signing up we automatically logs in the user 
            # login(request, user)                                             #login(HttpResponse,User)
            return redirect("main:employer")
        
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})

# view for signup page of employer
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
            messages.success(request, f"New account created: {username}")    #displaying the message that new account has been created
            
            # now after signing up we automatically logs in the user 
            login(request, user)                                             #login(HttpResponse,User)
            if user.is_student:
                return redirect("main:student_profile")
            else:
                return redirect("main:employer_profile")  
        
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})


# view for signup page of student
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
            messages.success(request, f"New account created: {username}")
            login(request, user)
            if user.is_student:
                return redirect("main:student")
            else:
                return redirect("main:employer")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            form=self.form_class(initial=self.initial)
            return render(request ,self.template_name,{'form':form})



#function for logging the user out of the current session
class logout_request(View):
    def get(self,request):
       logout(request)
       messages.info(request, "Logged out successfully!")
       return redirect("main:homepage") 


class login_request(View):
    form_class=AuthenticationForm
    initial={'key':'value'}
    template_name="main/login.html"

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
                messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
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











#fucntion for logging in the user
# def login_request(request):                                                            
    
#     if request.method == 'POST':                                             #if user hits the login button
#         form = AuthenticationForm(request=request, data=request.POST)
        # if form.is_valid():                                                  #if the form is valid
        #     username = form.cleaned_data.get('username')                     #saving the username form the form
        #     password = form.cleaned_data.get('password')                     #saving the password from the form
        #     user = authenticate(username=username, password=password)        #authenticating the user i.e. username and passwords match simultaneously with a user's profile in database
        #     if user is not None:                                             #basically means "if user is true i.e. if user is successfully authenticated"
        #         login(request, user)                                         #log the user into the session
        #         messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
        #         if user.is_student:
        #           return redirect("main:student")
        #         else:
        #           return redirect("main:employer")                               
        #     else:                                                            #if it fails to authenticate
        #         messages.error(request, "Invalid username or password.")     #display an error message

        # else:                                                                #if the form is not valid
        #     messages.error(request, "Invalid username or password.")         #display the error message

#     form = AuthenticationForm()
#     return render(request = request,
#                     template_name = "main/login.html",
#                     context={"form":form})


#function for register as student page
# def register_as_student(request):                                          
#     if request.method == "POST":
#         form = NewUserForm2(request.POST)
        # if form.is_valid():
        #     user = form.save()
        #     username = form.cleaned_data.get('username')
        #     messages.success(request, f"New account created: {username}")
        #     login(request, user)
        #     if user.is_student:
        #         return redirect("main:student")
        #     else:
        #         return redirect("main:employer")

        # else:
        #     for msg in form.error_messages:
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")

        #     return render(request = request,
        #                   template_name = "main/Student-Signup.html",
        #                   context={"form":form})

#     form = NewUserForm2
#     return render(request = request,
#                   template_name = "main/Student-Signup.html",
#                   context={"form":form})                      



 #function for register as employer page
# def register_as_employer(request):                                       
#     if request.method == "POST":                                                #if user hits the sign up button
#         form = NewUserForm1(request.POST)                                #mapping the submitted form to user creation form
        # if form.is_valid():                                                     #if the form filled is valid
        #     user = form.save()                                           #basically save the user(since user is a part of form,thus we save the form)
        #     username = form.cleaned_data.get('username')                     #getting the username from the form   
        #     messages.success(request, f"New account created: {username}")    #displaying the message that new account has been created
            
        #     # now after signing up we automatically logs in the user 
        #     login(request, user)                                             #login(HttpResponse,User)
        #     if user.is_student:
        #         return redirect("main:student")
        #     else:
        #         return redirect("main:employer")  
        
        # else:                                                 #if form is not valid or not filled properly               
        #     for msg in form.error_messages:                   
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

        #     return render(request = request,
        #                   template_name = "main/Employer-Signup.html",
        #                   context={"form":form})


#     form = NewUserForm1
#     return render(request = request,
#                   template_name = "main/Employer-Signup.html",
#                   context={"form":form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your MySite Account'
#             message = render_to_string('acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# view function for showing which students have applied for the internship
# def interns_applied(request):
#     return render(request=request,
#                   template_name="main/jobs_posted.html",
#                   context={"intern":Intern.objects.all()})


# view function for posting a job
# def post_a_job(request):                                      
#     if request.method == "POST":                                                #if user hits the sign up button
#         form = Job_Post(request.POST)                                #mapping the submitted form to user creation form
        # if form.is_valid():                                                     #if the form filled is valid
        #     job_profile = form.save(commit=False)  
        #     job_profile.username=request.user  
        #     job_profile.save()                                       #basically save the user(since user is a part of form,thus we save the form)
        #     username = form.cleaned_data.get('job_title')                     #getting the username from the form   
        #     messages.success(request, f"New Job created: {username}")    #displaying the message that new account has been created
            
        #     # now after signing up we automatically logs in the user 
        #     # login(request, user)                                             #login(HttpResponse,User)
        #     return redirect("main:employer")
        
        # else:                                                 #if form is not valid or not filled properly               
        #     for msg in form.error_messages:                   
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

        #     return render(request = request,
        #                   template_name = "main/post_job.html",
        #                   context={"form":form})


#     form = Job_Post()
#     return render(request = request,
#                   template_name = "main/post_job.html",
#                   context={"form":form}) 


# view function for form for applying for an internship
# def apply_for_job(request):
#     if request.method== "POST":
#         form = Apply_Job(request.POST)
        # if form.is_valid():
        #     intern_profile= form.save(commit=False)
            
        #     intern_profile.username=request.user
        #     intern_profile.save()
        #     #username = form.cleaned_data.get('intern_profile.username')                     #getting the username from the form   
        #     messages.success(request, f"{intern_profile.username} has succesully applied for this job")

        #     return redirect("main:student")
        # else:                                                 #if form is not valid or not filled properly               
        #     for msg in form.error_messages:                   
        #         messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

        #     return render(request = request,
        #                   template_name = "main/apply_for_job.html",
        #                   context={"form":form})


#     form = Apply_Job()
#     return render(request = request,
#                   template_name = "main/apply_for_job.html",
#                   context={"form":form}) 



# view function for adding a location
# def add_location(request):
#     if request.method== "POST":
#         form = Location(request.POST)
#         if form.is_valid():
#             loc= form.save(commit=False)
#             loc.save()
#             username = form.cleaned_data.get('location')                     #getting the username from the form   
#             messages.success(request, f"New Location {username} created")

#             return redirect("main:employer")
#         else:                                                 #if form is not valid or not filled properly               
#             for msg in form.error_messages:                   
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

#             return render(request = request,
#                           template_name = "main/location.html",
#                           context={"form":form})


#     form = Location()
#     return render(request = request,
#                   template_name = "main/location.html",
#                   context={"form":form}) 


# view function for adding a category
# def add_category(request):
#     if request.method== "POST":
#         form = Category(request.POST)
#         if form.is_valid():
#             cat= form.save(commit=False)
#             cat.save()
#             username = form.cleaned_data.get('category')                     #getting the username from the form   
#             messages.success(request, f"New Category {username} created")

#             return redirect("main:employer")
#         else:                                                 #if form is not valid or not filled properly               
#             for msg in form.error_messages:                   
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

#             return render(request = request,
#                           template_name = "main/category.html",
#                           context={"form":form})


#     form = Category()
#     return render(request = request,
#                   template_name = "main/category.html",
#                   context={"form":form}) 




# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# Create your views here.

# def add_profile(request):
#     if request.method == 'POST':
#         form = profileform(request.POST)
#         if form.is_valid():
#             profile_item = form.save(commit=False)
#             profile_item.save()
#             return redirect('/')

#     else:
#         form = profileform()        
#         return render(request,"main/addprofile.html",{'form':form})




# def register_as_employer(request):
#     if request.method == 'POST':
#         form = NewUserForm1(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string('main/acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = NewUserForm1()
#     return render(request, 'main/signup.html', {'form': form})


# def activate_account(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')



# from .forms import NewUserForm, profileform
# def login_as_student(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect("main:student")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request = request,
#                     template_name = "main/login.html",
#                     context={"form":form})                    


                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        #    Mahima's Code
# =======
# def account(request):
#     return render(request=request,template_name="main/account.html")


# def add_profile(request):
#     if request.method == 'POST':
#         form = profileform(request.POST)
#         if form.is_valid():
#             profile_item = form.save(commit=False)
#             profile_item.save()
#             return redirect('/')

#     else:
#         form = profileform()        
#         return render(request,"main/addprofile.html",{'form':form})
# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d

# =======
#     form = NewUserForm
# >>>>>>> 0c068883fa2efc525150809d3d31552b94896f8d
   