#A view function, or “view” for short, is simply a Python function that takes a web request 
#and returns a web response. This response can be the HTML contents of a Web page, or a redirect,
#or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, 
#note that you need to associate a view to a URL to see it as a web page.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm1,NewUserForm2
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.db.models import Value
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import Job_Post,Apply_Job,Location,Category
from .forms import NewUserForm1,EditProfileForm
from .forms import NewUserForm2
from . models import Job
@login_required
def add_category(request):
    if request.method== "POST":
        form = Category(request.POST)
        if form.is_valid():
            cat= form.save(commit=False)
            cat.save()
            user = form.cleaned_data.get('category')                     #getting the username from the form   
            messages.success(request, f"New Category {user} created")
            return internship_list(request)
    else:
        form = Category()
    return render(request,"main/category_form.html",{"form":form}) 


def add_location(request):
    if request.method== "POST":
        form = Location(request.POST)
        if form.is_valid():
            loc= form.save(commit=False)
            loc.save()
            username = form.cleaned_data.get('location')                     #getting the username from the form   
            messages.success(request, f"New Location {username} created")

            return internship_list(request)
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            return render(request = request,
                          template_name = "main/location.html",
                          context={"form":form})


    form = Location()
    return render(request = request,
                  template_name = "main/location.html",
                  context={"form":form}) 


def apply_for_job(request):
    if request.method== "POST":
        form = Apply_Job(request.POST)
        if form.is_valid():
            intern_profile= form.save(commit=False)
            #intern_profile.job_title=form.cleaned_data.get('job_title')
            intern_profile.username=request.user
            intern_profile.save()
            #username = form.cleaned_data.get('intern_profile.username')                     #getting the username from the form   
            messages.success(request, f"{intern_profile.username} has succesully applied for this job")

            return redirect("main:student")
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            return render(request = request,
                          template_name = "main/apply_for_job.html",
                          context={"form":form})


    form = Apply_Job()
    return render(request = request,
                  template_name = "main/apply_for_job.html",
                  context={"form":form}) 
#

@login_required
def internship_list(request):
    internship = Job.objects.filter(user=request.user)
    return render(request, 'main/postinternship_list.html', {'internship': internship})
    
#new

@login_required
def edit_all_internship(request):
    ProductFormSet = modelformset_factory(Job, fields=('job_title', 'category', 'location','job_duration','job_content','job_published','job_stipend'), extra=0)
    data = request.POST or None
    formset = ProductFormSet(data=data, queryset=Job.objects.filter(user=request.user))
    
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return internship_list(request)

    return render(request, 'main/postinternship_formset.html', {'formset': formset})

@login_required
def post_a_job(request):                                      
    if request.method == "POST":                                                #if user hits the sign up button
        form = Job_Post(request.user,request.POST)                                #mapping the submitted form to user creation form
        if form.is_valid():                                                     #if the form filled is valid
            job_profile = form.save(commit=False)  
            job_profile.user=request.user  
            job_profile.save()                                       #basically save the user(since user is a part of form,thus we save the form)
            user = form.cleaned_data.get('job_title')                     #getting the username from the form   
            messages.success(request, f"New Job created: {user}")    #displaying the message that new account has been created
            
            # now after signing up we automatically logs in the user 
            # login(request, user)                                             #login(HttpResponse,User)
            return internship_list(request)
        
    form = Job_Post(request.user)
    return render(request = request,
                  template_name = "main/postinternship_form.html",
                  context={"form":form}) 

 #view function for homepage 

def homepage(request):                                              
    return render(request=request,
                  template_name="main/home.html",
                  context={"jobs":Job.objects.all()})



#view function to display the jobs posted by the company
def jobs_list(request):
    # jobs=Job.objects.filter(user=request.user)
    return render(request=request,
                  template_name="main/jobs_list.html",
                  context={"jobs":Job.objects.all()}
                )                

#view function for student's profile

def student(request):                                                
    return render(request=request,
                  template_name="main/student_profile.html",
                  context={"jobs":Job.objects.all()}
                )

 #view function for employer's profile

def employer(request):                                              
    return render(request=request,
                  template_name="main/employer_profile.html",
                  context={"jobs":Job.objects.all()}
                )

def interns_applied(request):
    return render(request=request,
                  template_name="main/jobs_posted.html",
                  context={"intern":Intern.objects.all()})

 #function for register as employer page

def register_as_employer(request):                                       
    if request.method == "POST":                                                #if user hits the sign up button
        form = NewUserForm1(request.POST)                                #mapping the submitted form to user creation form
        if form.is_valid():                                                     #if the form filled is valid
            user = form.save()                                           #basically save the user(since user is a part of form,thus we save the form)
            username = form.cleaned_data.get('username')                     #getting the username from the form   
            messages.success(request, f"New account created: {username}")    #displaying the message that new account has been created
            
            # now after signing up we automatically logs in the user 
            login(request, user)                                             #login(HttpResponse,User)
            if user.is_student:
                return redirect("main:student")
            else:
                return redirect("main:employer")  
        
        else:                                                 #if form is not valid or not filled properly               
            for msg in form.error_messages:                   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")   #displaying the error messages

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})


    form = NewUserForm1
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

 #function for register as student page
def register_as_student(request):                                          
    if request.method == "POST":
        form = NewUserForm2(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm2
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})                      


#function for logging the user out of the current session

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage") 

#fucntion for logging in the user

def login_request(request):                                                            
    
    if request.method == 'POST':                                             #if user hits the login button
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():                                                  #if the form is valid
            username = form.cleaned_data.get('username')                     #saving the username form the form
            password = form.cleaned_data.get('password')                     #saving the password from the form
            user = authenticate(username=username, password=password)        #authenticating the user i.e. username and passwords match simultaneously with a user's profile in database
            if user is not None:                                             #basically means "if user is true i.e. if user is successfully authenticated"
                login(request, user)                                         #log the user into the session
                messages.info(request, f"You are now logged in as {username}")    #display a message that user is logged in
                #if user.is_student:
                  #return redirect("main:student")
                #else:
                return redirect("main:homepage")                               
            else:                                                            #if it fails to authenticate
                messages.error(request, "Invalid username or password.")     #display an error message

        else:                                                                #if the form is not valid
            messages.error(request, "Invalid username or password.")         #display the error message

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('main:view_profile'))
        else:
            return redirect(reverse('main:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'main/change_password.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return view_profile(request)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'main/edit.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'main/home.html', args)
                         
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
         