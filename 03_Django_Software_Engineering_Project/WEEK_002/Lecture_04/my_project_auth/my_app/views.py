from django.shortcuts import render,redirect
from .forms import SignUpForm,Change_User_Data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def home(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            
    else:
         form=SignUpForm()
    return render(request, 'home.html',context={'form':form})

def signup(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,"Your account has been Created")
                form.save(commit=True)
                print(form.cleaned_data)
                
        else:
            form=SignUpForm()
        return render(request,'signup.html',context={'form':form})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                messages.success(request,"Your account has been Created")
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('profile') 
                
                
        else:
            form=AuthenticationForm()
        return render(request,'login.html',context={'form':form,'user':request.user})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',context={'user':request.user})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'change_password.html',context={'form':form})
    else:
        return redirect('login')

def password_change_set(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
            
        else:
            form=SetPasswordForm(request.user)
        return render(request,'change_password.html',context={'form':form})
    else:
        return redirect('login')
    

def change_user_data(request):
    if  request.user.is_authenticated:
        if request.method =='POST':
            form=Change_User_Data(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,"Your data has been Changed")
                form.save(commit=True)
                
                
        else:
            form=Change_User_Data(instance=request.user)
        return render(request,'signup.html',context={'form':form})
    else:
        return redirect('login')
        

