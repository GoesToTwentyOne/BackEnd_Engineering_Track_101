from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse(
        '''
            <h1> From contact page</h1>
            <a href="/my_app/about">About</a>
            <a href="/my_app_two/feedback">Feedback</a>
            <a href="/my_app_two/courses">Courses</a>
        '''
        )
def about(request):
    return HttpResponse(
        '''
        <h1>From about page</h1>
        <a href="/my_app/contact">Contact</a>
        <a href="/my_app_two/feedback">Feedback</a>
        <a href="/my_app_two/courses">Courses</a>
        '''
        )