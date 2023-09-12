# Build in User Model
https://docs.djangoproject.com/en/4.2/ref/contrib/auth/
# Build in UserCreation and User Change form 
https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/



## Sign UP 
```python
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm,UserChangeForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
```
## Sign UP Input
```python
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block content %}
{% if messages %}
{% for message in messages %}
{% comment %} <small {% if message.tags %} class="{{message.tags}}" {% endif %}></small> {% endcomment %}
<button type="button" class="btn btn-primary">{{ message }}</button>
{% endfor %}
{% endif %}


<h1 style="text-align: center;">Register Form</h1>
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    <form method='POST' action="" style="width: 40%; height: 100%;" novalidate>
        {% csrf_token %}
        {{ form | crispy }}
   
            {% comment %} {% for fm in form %}
            {{fm.label_tag }}
            {{fm}}
            {{fm.errors}}
            {% endfor %}  {% endcomment %}
        # Add any additional form fields, labels, and error messages as needed 
        <br/>
        <button type="submit" class="btn btn-primary">Submit</button>
        <br/>
        <small>Already have an account.Please Login  <a href="{% url 'login' %}" >Login</a><small>
        
    </form>
</div>


{% endblock %}
```
## Sign up view
```python
def signup(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,"Your account has been Created")
                form.save(commit=True)
                print(form.cleaned_data)
                
        else:
            form=SignUpForm()
        return render(request,'signup.html',context={'form':form})
    else:
        return redirect('profile')

```

## Login views
```python
from django.shortcuts import render,redirect
from .forms import SignUpForm,Change_User_Data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                messages.success(request,"Your account has been Created")
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('profile') 
                
                
        else:
            form=AuthenticationForm()
        return render(request,'login.html',context={'form':form,'user':request.user})
    else:
        return redirect('profile')
```
## Login Input
```python
{% if form.non_field_errors %}
    {% for error in form.non_field_errors %}
    <div class="alert alert-danger" role="alert">
        {{ error }}
    </div>
    {% endfor %}
{% endif %}
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    <form method='POST' action="" style="width: 40%; height: 100%;" novalidate>
        {% csrf_token %}
        {{ form | crispy }}
   
            {% comment %} {% for fm in form %}
            {{fm.label_tag }}
            {{fm}}
            {{fm.errors}}
            {% endfor %}  {% endcomment %}
        <br/>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
```

## Password Change with Old Password
```python
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'change_password.html',context={'form':form})
    else:
        return redirect('login')

```
```python
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block content %}
{% if messages %}
{% for message in messages %}
{% comment %} <small {% if message.tags %} class="{{message.tags}}" {% endif %}></small> {% endcomment %}
<button type="button" class="btn btn-primary">{{ message }}</button>
{% endfor %}
{% endif %}


<h1 style="text-align: center;">Password Change  Form</h1>
{% if form.non_field_errors %}
    {% for error in form.non_field_errors %}
    <div class="alert alert-danger" role="alert">
        {{ error }}
    </div>
    {% endfor %}
{% endif %}
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    <form method='POST' action="" style="width: 40%; height: 100%;" novalidate>
        {% csrf_token %}
        {{ form | crispy }}
   
            {% comment %} {% for fm in form %}
            {{fm.label_tag }}
            {{fm}}
            {{fm.errors}}
            {% endfor %}  {% endcomment %}
    
        <br/>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>


{% endblock %}

```
## Password Change without Old Password
```python
def password_change_set(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
            
        else:
            form=SetPasswordForm(request.user)
        return render(request,'change_password.html',context={'form':form})
    else:
        return redirect('login')
```
## Chage User Data | Update Profile
```python
## build in userchange form
class Change_User_Data(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
```
```python
# views
def change_user_data(request):
    if  request.user.is_authenticated:
        if request.method =='POST':
            form=Change_User_Data(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,"Your data has been Changed")
                form.save(commit=True)
                
                
        else:
            form=Change_User_Data(instance=request.user)
        return render(request,'signup.html',context={'form':form})
    else:
        return redirect('login')
        

```
```python
#form
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}
{% if messages %}
{% for message in messages %}
{% comment %} <small {% if message.tags %} class="{{message.tags}}" {% endif %}></small> {% endcomment %}
<button type="button" class="btn btn-primary">{{ message }}</button>
{% endfor %}
{% endif %}
<h1 style="text-align: center;">Chnage User data  Form</h1>
<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    <form method='POST' action="" style="width: 40%; height: 100%;" novalidate>
        {% csrf_token %}
        {{ form | crispy }}
   
            {% comment %} {% for fm in form %}
            {{fm.label_tag }}
            {{fm}}
            {{fm.errors}}
            {% endfor %}  {% endcomment %}
      
        <br/>
        <button type="submit" class="btn btn-primary">Submit</button>
        <br/>
        
    </form>
</div>
{% endblock %}
```