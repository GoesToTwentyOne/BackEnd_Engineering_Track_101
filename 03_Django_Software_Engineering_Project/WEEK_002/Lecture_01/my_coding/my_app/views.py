from django.shortcuts import render,redirect
from . import models

# Create your views here.

def home(request):
    data=models.Student.objects.all()
    return render(request,'index.html',context={'data':data})
def delete_student(request,roll):
    std=models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')

