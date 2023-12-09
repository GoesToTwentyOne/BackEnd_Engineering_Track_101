from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
def a(request):
    return HttpResponse("A")
def b(request):
    return HttpResponse("B")