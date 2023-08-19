from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def love(request):
    return render(request,'love.html')
