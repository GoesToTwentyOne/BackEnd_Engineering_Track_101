from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("I'm from about page")
def firstapp(request):
    return HttpResponse("I'm from firstapp page")
