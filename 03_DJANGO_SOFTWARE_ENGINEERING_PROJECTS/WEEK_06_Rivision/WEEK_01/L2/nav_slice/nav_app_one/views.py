from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def one_home(request):
    two_course_url = reverse('two_course')
    one_about_url = reverse('One_about')
    one_contact_url = reverse('one_contact')

    html_content = f'''
        I'm one home
        <a href="{two_course_url}">two_course</a>
        <a href="{one_about_url}">one_about</a>
        <a href="{one_contact_url}">one_contact</a>
        
    '''

    return HttpResponse(html_content)
def one_contact(request):
    return HttpResponse('''
                        I'm one Conatact
                        <a href="{% url 'One_home' %}">one_home</a>
                        <a href="{% url 'One_about' %}">one_about</a>
                        <a href="{% url 'two_course' %}">two_course</a>
                        ''')
def one_about(request):
    return HttpResponse('''
                        I'm one About
                        <a href="{% url 'One_home' %}">one_home</a>
                        <a href="{% url 'One_contact' %}">one_contact</a>
                        <a href="{% url 'two_course' %}">two_course</a>
                        ''')