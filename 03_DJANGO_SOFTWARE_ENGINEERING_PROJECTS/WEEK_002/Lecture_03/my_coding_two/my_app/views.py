from django.shortcuts import render
from . forms import studentForm
from .models import Studentinfo,Teacherinfo,Person,Passport


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


def show(request):
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
#one to one relationship
def show_data_one_to_one(request):
    passt=Passport.objects.get(passport_number=454578)
    person=passt.passport.all()
    print(person.city)
    
  



# many to many relations
def show_data(request):
    # one teacher has students
    teacher = Teacherinfo.objects.get(name="Hasan")
    students=teacher.student_user.all()
    for student in students:
        print(student.name)

    # one student has teachers
    student = Studentinfo.objects.get(name="Nihad")
    #teachers = student.teacherinfo_set.all()
    teachers = student.teacherinfo.all()
    for teacher in teachers:
        print(teacher.name)
    return render(request, 'show_data.html')





