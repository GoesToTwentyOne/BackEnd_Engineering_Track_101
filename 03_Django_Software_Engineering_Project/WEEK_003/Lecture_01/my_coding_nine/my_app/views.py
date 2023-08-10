from django.shortcuts import render
from datetime import datetime,timedelta
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = render(request,'home.html')
    response.set_cookie('name','alex',max_age=30)
    response.set_cookie('name','alex',expires=datetime.utcnow()+timedelta(days=10))
    return response
def get_cookies(request):
    name=request.COOKIES.get('name')
    return render(request,'get_cookies.html',context={'name':name})

def delete_cookies(request):
    response=render(request,'delete_cookies.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name': 'alex',
        'age': 18,
        'year': 2023,
    }
    # Update the session with the provided data
    request.session.update(data)
    # Save the session data
    request.session.save()
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date() )
    return render(request, 'set_session.html')

def get_sessions(request):
    name=request.session.get('name')
    age=request.session.get('age')
    year=request.session.get('year')
    return render(request,'get_sessions.html',context={'name':name, 'age':age, 'year':year})


def delete_session(request):
    # del request.session['name']
    # request.session.clear_expired()
    request.session.flush()
    return render(request,'delete_session.html')

def session_expired(request):
    if 'name' in request.session:
        name=request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'session_running.html')
    else:
        return HttpResponse("Your session expired")
        