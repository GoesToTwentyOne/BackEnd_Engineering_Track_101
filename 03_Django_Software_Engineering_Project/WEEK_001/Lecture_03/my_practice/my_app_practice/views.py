from django.shortcuts import render

# Create your views here.
def my_app(request):
    return render(request,'./index.html')