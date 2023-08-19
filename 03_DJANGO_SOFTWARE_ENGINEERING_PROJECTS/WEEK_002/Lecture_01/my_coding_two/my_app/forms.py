from django import forms
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
   
