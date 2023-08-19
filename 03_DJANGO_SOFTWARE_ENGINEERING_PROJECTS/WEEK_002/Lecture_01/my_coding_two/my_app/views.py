from django.shortcuts import render
from . forms import studentForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request, 'home.html', context={'form': form})
        # else:
        #     return render(request, 'my_app/validateForm.html', context={'form': form})
    else:
        form = studentForm()
    return render(request, 'home.html', context={'form': form})



