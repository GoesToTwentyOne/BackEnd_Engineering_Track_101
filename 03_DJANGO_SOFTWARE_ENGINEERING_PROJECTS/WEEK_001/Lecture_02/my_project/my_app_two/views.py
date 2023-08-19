from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse(
        '''
        <h1>From Courses Page</h1>
        <a href="/my_app_two/feedback">Feedback</a>
        <a href="/my_app/about">About</a>
        <a href="/my_app/contact">Contact</a>

        '''
    )
def feedback(request):
    return HttpResponse(
        
        '''
        <h1>From Feedback page</h1>
        <a href="/my_app_two/courses">Courses</a>
        <a href="/my_app/about">About</a>
        <a href="/my_app/contact">Contact</a>
        '''
        
    )