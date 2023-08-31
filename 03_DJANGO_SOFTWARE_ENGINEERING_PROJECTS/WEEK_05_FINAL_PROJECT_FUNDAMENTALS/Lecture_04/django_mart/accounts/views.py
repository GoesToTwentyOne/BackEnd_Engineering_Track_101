from django.shortcuts import render,redirect
from accounts.forms import UserRegistrationForm
from django.contrib.auth import login,logout,authenticate
from cart.models import Cart,CartItem
# Create your views here.
def get_session_create(request):
    if not request.session.session_key:
        request.session.create()
        return request.session.session_key
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
        session_id=get_session_create(request)
        cart_id=Cart.objects.get(cart_id=session_id)
        is_cart_item_exist=CartItem.objects.filter(cart=cart_id).exists()
        if is_cart_item_exist:
            cart_item=CartItem.objects.filter(cart=cart_id)
            for item in cart_item:
                item.user=user
                item.save()
        
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/signin.html')