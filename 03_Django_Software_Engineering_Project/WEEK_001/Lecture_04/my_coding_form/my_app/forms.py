from typing import Any, Dict
from django import forms
from django.core import validators
class contactForm(forms.Form):
    name=forms.CharField(label="User Name",initial="Nihad",help_text="must be at least 10 characters",required=True,disabled=False)
    #widget=forms.Input(attrs={'id':"name",'class':"Class",'placeholder':"Enter your value"}))
    file=forms.FileField()
    
    email=forms.EmailField(label="User Email")
    age=forms.IntegerField(label="Age")
    weight=forms.FloatField(label="Weight")
    balance=forms.DecimalField(label="balance")
    dob=forms.DateField(label="DOB",widget=forms.DateTimeInput(attrs={'type':'date'}))
    appoinment=forms.DateTimeField(label="appoinment",widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOOSE=[('M',"Medium"),("S","Small"),("B","Big")]
    size=forms.ChoiceField(label="Size", choices=CHOOSE,widget=forms.RadioSelect)
    MEAL=[('P',"Peparonic"),("M","Meat"),("J","Juice")]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)

    check=forms.BooleanField(label="Check")
def custom_name_func(value):
    if len(value)<7:
        return forms.ValidationError(message="Please enter a valid name with up to 7 characters")

class studentForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Name must be at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("not correct convension .com format")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()  # Call the parent class clean() to get the cleaned data
    #     valname = cleaned_data['name']
    #     valemail = cleaned_data['email']

    #     if valname and len(valname) < 10:
    #         raise forms.ValidationError("Name must be at least 10 characters")

    #     if valemail and '.com' not in valemail:
    #         raise forms.ValidationError("Not the correct '.com' email format")

    #     return cleaned_data  # Always return the cleaned data at the end of the clean() method

        name = forms.CharField(validators=[validators.MaxLengthValidator(45,message="max length must be 45 characters"),validators.MinLengthValidator(5,message="Atleast 5 char")])
        email = forms.EmailField(validators=[validators.EmailValidator(message="Please enter a valid email address")])
        age=forms.IntegerField(validators=[validators.MaxValueValidator(28,message="max value must be 28 "),validators.MinValueValidator(25,message="atleast 25 ")])
        file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="only pf files are allowed")])

        custom_name=forms.CharField(validators=[custom_name_func])

class password_validation(forms.Form):
     name = forms.CharField(validators=[validators.MaxLengthValidator(45,message="max length must be 45 characters"),validators.MinLengthValidator(5,message="Atleast 5 char")])
     password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'type':'password'}))
     confirm_password=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'type':'password'}))

     def clean(self):
          cleaned_data=super().clean()
          val_name=cleaned_data['name']
          val_password=cleaned_data['password']
          val_confirm_password=cleaned_data['confirm_password']
          if val_password != val_confirm_password:
               raise forms.ValidationError("Passwords do not match")
          if len(val_name) <7 :
               raise forms.ValidationError("Please enter a valid name with up to 7 characters")







