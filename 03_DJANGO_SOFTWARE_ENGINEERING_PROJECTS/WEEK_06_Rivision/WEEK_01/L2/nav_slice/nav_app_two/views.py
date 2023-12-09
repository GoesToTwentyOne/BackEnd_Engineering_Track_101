from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def two_home(request):
    one_contact_url = reverse('One_contact')
    one_about_url = reverse('One_about')

    html_content = f'''
        I'm Two home
        <a href="{one_contact_url}">one_contact</a>
        <a href="{one_about_url}">one_about</a>
    '''

    return HttpResponse(html_content)

def two_course(request):
    one_home_url = reverse('One_home')
    one_about_url = reverse('One_about')

    html_content = f'''
        I'm Two Course
        <a href="{one_home_url}">one_home</a>
        <a href="{one_about_url}">one_about</a>
    '''

    return HttpResponse(html_content)
