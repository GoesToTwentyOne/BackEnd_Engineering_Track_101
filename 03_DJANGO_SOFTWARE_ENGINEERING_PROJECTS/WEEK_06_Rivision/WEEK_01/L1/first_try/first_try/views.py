from django.http import HttpResponse
def home(request):
    return HttpResponse("Hi I'm Nihad")
def about(request):
    return HttpResponse("about")