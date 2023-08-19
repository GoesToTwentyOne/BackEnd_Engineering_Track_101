from django.shortcuts import render
from . forms import contactForm,studentForm,password_validation
# Create your views here.
text=[{'Id':101,'course':'c++','Teacher':'Alex Smith'},{'Id':102,'course':'databases','Teacher':'Gorkie'},{'Id':103,'course':'django','Teacher':'Bruno'}]
def home(request):
    return render(request, './my_app/index.html',context={'name':"My name is Md. Nihad Hossain",'marks':96,'courses':text})
def about(request):
        if request.method == 'POST':
            name=request.POST.get('user_name')
            email=request.POST.get('user_email')
            select=request.POST.get('select')

            return render(request, './my_app/about.html',context={'name':name,'email':email, 'select':select})
        
        return render(request, './my_app/about.html')

def submit_form(request):
    return render(request, './my_app/form.html')



def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)  # Creating an instance of the 'ContactForm' with POST data and files

        if form.is_valid():  # Checking if the form data is valid
            # Accessing the 'file' field data (assuming there's a 'file' field in the form)
            f_file = form.cleaned_data['file']
            
            # Saving the uploaded file
            with open('./my_app/upload/' + f_file.name, 'wb+') as destination:
                for chunk in f_file.chunks():
                    destination.write(chunk)

            # Printing cleaned (validated) form data (optional)
            print(form.cleaned_data)

            # Rendering the 'contact.html' template with the form instance as context data
            return render(request, 'my_app/contact.html', context={'form': form})

    else:
        # Creating an instance of the 'ContactForm' without any data when request method is not 'POST'
        form = contactForm()

    # Rendering the 'contact.html' template with the form instance as context data
    return render(request, 'my_app/contact.html', context={'form': form})

def student_data(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/validateForm.html', context={'form': form})
        # else:
        #     return render(request, 'my_app/validateForm.html', context={'form': form})
    else:
        form = studentForm()
    return render(request, 'my_app/validateForm.html', context={'form': form})

def password(request):
    if request.method == 'POST':
        form = password_validation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/passwordvalidation.html', context={'form': form})
        # else:
        #     return render(request, 'my_app/validateForm.html', context={'form': form})
    else:
        form = password_validation()
    return render(request, 'my_app/passwordvalidation.html', context={'form': form})

