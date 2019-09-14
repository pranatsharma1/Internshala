from django.shortcuts import render, redirect
from .models import Job,UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm1,NewUserForm2
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import  EditProfileForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm




# Create your views here.



def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"jobs":Job.objects.all()})
#new
def student_profile(request):
    return render(request=request,
                  template_name="main/student_profile.html",
                  context={"jobs":Job.objects.all()})

def company_profile(request):
    return render(request=request,
                  template_name="main/company_profile.html",
                  context={"jobs":Job.objects.all()})

def student(request):
    return render(request=request,
                  template_name="main/index1.html",
                  context={"jobs":Job.objects.all()}
                )

def employer(request):
    return render(request=request,
                  template_name="main/index2.html",
                  context={"jobs":Job.objects.all()}
                )


def register_as_employer(request):
    if request.method == "POST":
        form = NewUserForm1(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            # user.is_staff=True
            return redirect("main:company_profile")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})


    form = NewUserForm1
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form}) 




def register_as_student(request):
    if request.method == "POST":
        form = NewUserForm2(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:student_profile")

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

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage") 

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})


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

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('main:view_profile'))
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
    return render(request, 'main/account.html', args)

#new code
'''
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('main:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })'''
    