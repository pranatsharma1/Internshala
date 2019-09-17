from django.shortcuts import render, redirect
from .models import Job,UserProfile,post_job
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm1,NewUserForm2
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import  EditProfileForm,LocationForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import UserForm,EmployerForm,IntershipCategoryForm
from .forms import CategoryForm, ProductForm,StudentApplyForm
from .models import Category, Products,Location,StudentApply
from django.forms import modelformset_factory
from django.db.models import Value


def list_of_category(request):
    category = Category.objects.values('name').distinct()
    print(category)
    return render(request, 'main/category_all.html', {'category': category})

def Studentprofile(request):
    products = Products.objects.all()
    #"category":Category.objects.all()
    print(products)
    return render(request, 'main/student_profile.html', {'products': products})

@login_required
def products_list(request):
    products = Products.objects.filter(user=request.user)
    return render(request, 'main/products_list.html', {'products': products})


@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.user, request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return products_list(request)
    else:
        form = ProductForm(request.user)
    return render(request, 'main/product_form.html', {'form': form})


@login_required
def new_Location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return products_list(request)
    else:
        form = LocationForm()
    return render(request, 'main/location_form.html', {'form': form})

@login_required
def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return products_list(request)
    else:
        form = CategoryForm()
    return render(request, 'main/category_form.html', {'form': form})

@login_required
def student_apply(request):
    if request.method == 'POST':
        form = StudentApplyForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return products_list(request)
    else:
        form = CategoryForm()
    return render(request, 'main/apply_form.html', {'form': form})


@login_required
def edit_all_products(request):
    ProductFormSet = modelformset_factory(Products, fields=('name', 'Start_date', 'Duration','Stipend','category','location','student'), extra=0)
    data = request.POST or None
    formset = ProductFormSet(data=data, queryset=Products.objects.filter(user=request.user))
    for form in formset:
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
        form.fields['location'].queryset = Location.objects.filter(user=request.user)
        form.fields['student'].queryset = StudentApply.objects.filter(user=request.user)

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return products_list(request)

    return render(request, 'main/products_formset.html', {'formset': formset})
    #new
'''  
@login_required
def internship_list(request):
    products = internship_post.objects.filter(user=request.user)
    return render(request, 'main/internship_list.html', {'products': products})


@login_required
def new_internship(request):
    if request.method == 'POST':
        form = PostForm(request.user, request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return internship_list(request)
    else:
        form = PostForm(request.user)
    return render(request, 'main/internship_form.html', {'form': form})


@login_required
def internship_new_category(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return internship_list(request)
    else:
        form = CategoriesForm()
    return render(request, 'main/internship_category_form.html', {'form': form})


@login_required
def edit_all_internship(request):
    PostFormSet = modelformset_factory(internship_post, fields=('name','Start_date','Duration','Stipend','category', 'location'), extra=0)
    data = request.POST or None
    formset = PostFormSet(data=data, queryset=internship_post.objects.filter(user=request.user))
    for form in formset:
        form.fields['internship_post'].queryset = internship_post.objects.filter(user=request.user)

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return internship_list(request)

    return render(request, 'main/internship_formset.html', {'formset': formset})
    '''
#new
def homepage(request):
    return render(request=request, template_name="main/home.html", 
    context={"jobs":Job.objects.all(),"location":Location.objects.values('name').distinct(),"category":Category.objects.values('name').distinct()})
#distinct is using for showing the distinct field not duplicates
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
            return redirect("main:homepage")

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
            return Studentprofile(request)
            #render(request, 'main/student_profile.html')

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
                if user.is_student:
                    return Studentprofile(request)
                    # redirect("main:student_profile")
                else:
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
    return render(request, 'main/account.html', args)



def postform(request):
 
    if request.method == "POST":
        form = IntershipCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:homepage')
 
    else:
        form = IntershipCategoryForm()
        return render(request, "main/category.html", {'form': form})
#new
'''
class HomeView(TemplateView):
    template_name= 'main/home.html' #only to remove hardcoded

    def get(self,request):
        form = HomeForm()
        posts = post_job.objects.all()
        context = {'form':form,'posts':posts}
        return render(request,self.template_name,context)


    def post(self,request):
        form = HomeForm(request.POST)    
        if form.is_valid():
            post = form.save(commit=False)
            post.User = request.User
            post.save()

            text = form.cleaned_data['post']    
            form = HomeForm()
            return redirect( 'main:home')

        args ={'form': form, 'text': text}  
        return render(request, self.template_name, args)
'''
#new

