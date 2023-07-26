from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello I'm from response")
def about(request):
    return HttpResponse("I am from about")