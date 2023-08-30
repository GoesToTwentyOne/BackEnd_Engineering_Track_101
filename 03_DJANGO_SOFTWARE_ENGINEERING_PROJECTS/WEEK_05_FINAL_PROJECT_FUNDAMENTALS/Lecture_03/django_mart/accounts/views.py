from django.shortcuts import render,redirect
from accounts.forms import UserRegistrationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def register(request):
    form=UserRegistrationForm()
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'accounts/register.html',context={'form':form})

def profile(request):
    return render(request, 'accounts/dashboard.html')

def user_logout(request):
    logout(request)
    return render(request, 'accounts/signin.html')

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/signin.html')