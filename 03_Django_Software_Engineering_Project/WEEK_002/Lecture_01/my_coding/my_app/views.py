from django.shortcuts import render

# Create your views here.
text=[{'Id':101,'course':'c++','Teacher':'Alex Smith'},{'Id':102,'course':'databases','Teacher':'Gorkie'},{'Id':103,'course':'django','Teacher':'Bruno'}]
def home(request):
    return render(request, './my_app/index.html',context={'name':"My name is Md. Nihad Hossain",'marks':96,'courses':text})
def about(request):
    return render(request, './my_app/about.html',context={'author':'Sakib Al Hasan'})