from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from login.forms import CustomerRegistrationForm, ProfileForm, loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from login.models import Customer
from . import forms
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.
def login_user(request):
   


    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
           
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration.html', {'form': form, 'title':'register here'})
def Profile(request):
    form={}
    if request.user.is_authenticated:
        if request.method=="POST":
            form = ProfileForm(request.POST)
        
            if form.is_valid():
                user =request.user
                name = form.cleaned_data['name']
                mobile = form.cleaned_data['mobile']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                zipcode = form.cleaned_data['zipcode']
                state = form.cleaned_data['state']
                res = Customer(user = user , name = name , mobile=mobile ,locality=locality ,city = city ,zipcode = zipcode ,state =state)
                res.save()  
                messages.success(request ,'Profile Created Successfully!!')
            return render(request ,'profile.html',{'form':form , 'active':'btn-primary'}) 
        else:
            form = ProfileForm() 
    return render(request ,'profile.html',{'form':form , 'active':'btn-primary'})  
@login_required  
def address(request):
    addr = Customer.objects.filter(user = request.user)

    return render(request,'address.html',{'addr':addr ,  'active':'btn-primary'})       
# def logout(request):
#     if request.user.is_authenticated==True:
#         try:
#             logout(request)
#             messages.success(request,'Logout successfully')
#         except Exception as e:
#             messages.warning(request,'Something Went wrong !')
#             return redirect('login')
#     else:
#         return redirect('login')
#     return redirect('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            return redirect('login')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'resetpassword.html', {
        'form': form
    })

def forgot(request):
    return render(request, 'forgot.html')    

def resetpassword(request):
    return render(request,'resetpassword.html')  