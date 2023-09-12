# README.md - Django Models and ModelForm

This README provides an overview of the key components and operations related to Django models and ModelForms in our Django project.

## Models Definition

In our Django project, we have defined a model called `Student` in the following Python file:

```python
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=25)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    address2=models.TextField(default="Dhaka")
    def __str__(self) -> str:
        return f" Roll: {self.roll} -- Name: {self.name} -- Address: {self.address}"
```

This `Student` model represents student information with fields such as `name`, `roll`, `address`, and `address2`.

## Retrieving Data From Database

To retrieve data from the database and display it on a webpage, we have defined a view function called `home`:

```python
def home(request):
    data = models.Student.objects.all()
    return render(request, 'index.html', context={'data': data})
```

This view function fetches all student records from the `Student` model and passes them to an HTML template for rendering.

## Deleting Data From Database

To delete a student record from the database, we have defined a view function called `delete_student`:

```python
def delete_student(request, roll):
    std = models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')
```

We also have a corresponding URL pattern to handle delete requests:

```python
path('delete/<int:roll>', views.delete_student, name="delete_student"),
```

This URL pattern allows us to delete a student record by specifying the roll number in the URL.

## ModelForm Definition

In addition to the `Student` model, we have defined a model called `studentModel` and a ModelForm called `studentForm` for handling student data:

```python
from . import models
class studentForm(forms.ModelForm):
    class Meta:
        model=models.studentModel
        # fields=['name','rollno','email','password']
        fields='__all__'
        exclude=['password']
        labels={
            'name': 'Student Name',
            'email': 'Student Email'
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'rollno': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
        help_texts={
            'name': 'Student Name',
            'email': 'Student Email',
            'password': '<PASSWORD>'
        }
        error_messages={
            'name': {
              'required': 'Student Name is required',
              'max_length': 'Student Name must be less than 100 characters'
            },
        }
```

The `studentForm` is used for data input and validation, while the `studentModel` defines the structure of the student data.

## Saving Data to the Database Using ModelForm and Model

To save student data to the database, we have a view function named `home` that handles both GET and POST requests. When a POST request is received with valid data, it saves the data to the database:

```python
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
```

This view function creates a `studentForm` instance, validates the data, and saves it to the database if it's valid. It also handles GET requests to display the form for data input.

These are the main components and operations related to models and ModelForms in our Django project. You can refer to the code snippets and comments above for more details and implementation.