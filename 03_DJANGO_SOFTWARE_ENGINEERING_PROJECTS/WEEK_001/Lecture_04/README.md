# Normal HTML Form with Input Validation

This README provides information about a normal HTML form with input validation for a web application. 

## Form Structure
```html
<div style="width: 50%; height: 500px; margin: auto;" class="pt-5" >
    <h1>Form Input Validation</h1>
    <form method="POST" action="/my_app/about/">
        {% csrf_token %}
        <div class="mb-3">
            <label for="exampleInputName" class="form-label">Name</label>
            <input type="text" class="form-control" id="exampleInputName" aria-describedby="emailHelp" name="user_name">
        </div>
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="user_email">
        </div>
        <select class="form-select" multiple aria-label="Multiple select example" name="select">
            <option selected>Rating</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

This HTML form consists of fields for entering a user's name, email address, and selecting a rating. It utilizes Bootstrap classes for styling and includes CSRF protection.

## Handling Form Data
```python
def about(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        select = request.POST.get('select')
        return render(request, './my_app/about.html', context={'name': name, 'email': email, 'select': select})
    return render(request, './my_app/about.html')
```


# Django Build Form API

This README provides information about a Django-based form API for building and processing user input.

## Form Definition

To create a form, a Django `contactForm` class is defined in Python. This form consists of two fields: `name` for the user's name and `email` for the user's email address.

```python
class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
```

## HTML Form

The form is rendered using HTML and includes CSRF protection. It utilizes the `crispy` template tag to improve the form's presentation.

```html
<form method="POST" style="width: 50%; height: 500px; margin: auto;" class="pt-5">
    {% csrf_token %}
    {{ form }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

The form fields are displayed with labels, and a submit button is provided for user interaction.

## Form Processing

To handle form submissions, a view function `contactForm` is defined in Python. This function takes a `request` object, processes the form data, and renders the 'contact.html' template.

```python
def contactForm(request):
    form = contactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/contact.html', context={'form': form})
    else:
        form = contactForm()  # Instantiate a new form if the request method is not POST
    return render(request, 'my_app/contact.html', context={'form': form})
```


# Django Build Form API with Crispy Form Package 

This README provides information about a Django-based form API for building and processing user input.

## Form Definition

To create a form, a Django `contactForm` class is defined in Python. This form consists of two fields: `name` for the user's name and `email` for the user's email address.

```python
class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
```

## HTML Form

The form is rendered using HTML and includes CSRF protection. It utilizes the `crispy` template tag to improve the form's presentation.

```html
{% load crispy_forms_tags%}
<form method="POST" style="width: 50%; height: 500px; margin: auto;" class="pt-5" >
    {% csrf_token %}
    {{ form | crispy }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

The form fields are displayed with labels, and a submit button is provided for user interaction.

## Form Processing

To handle form submissions, a view function `contactForm` is defined in Python. This function takes a `request` object, processes the form data, and renders the 'contact.html' template.

```python
def contactForm(request):
    form = contactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/contact.html', context={'form': form})
    else:
        form = contactForm()  # Instantiate a new form if the request method is not POST
    return render(request, 'my_app/contact.html', context={'form': form})
```

# More Advance widget  Field Django Build Form API with Crispy Form Package 

This README provides information about a Django-based form API for building and processing user input.

## Form Definition

To create a form, a Django `contactForm` class is defined in Python. This form consists of two fields: `name` for the user's name and `email` for the user's email address.

```python
class contactForm(forms.Form):
    name=forms.CharField(label="User Name",initial="Nihad",help_text="must be at least 10 characters",required=True,disabled=False)
    #widget=forms.Input(attrs={'id':"name",'class':"Class",'placeholder':"Enter your value"}))
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
```

## HTML Form

The form is rendered using HTML and includes CSRF protection. It utilizes the `crispy` template tag to improve the form's presentation.

```html
{% load crispy_forms_tags%}
<form method="POST" style="width: 50%; height: 500px; margin: auto;" class="pt-5" >
    {% csrf_token %}
    {{ form | crispy }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

The form fields are displayed with labels, and a submit button is provided for user interaction.

## Form Processing

To handle form submissions, a view function `contactForm` is defined in Python. This function takes a `request` object, processes the form data, and renders the 'contact.html' template.

```python
def contactForm(request):
    form = contactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/contact.html', context={'form': form})
    else:
        form = contactForm()  # Instantiate a new form if the request method is not POST
    return render(request, 'my_app/contact.html', context={'form': form})
```



# File upload Django Build Form API with Crispy Form Package 

This README provides information about a Django-based form API for building and processing user input.

## Form Definition

To create a form, a Django `contactForm` class is defined in Python. This form consists of two fields: `name` for the user's name and `email` for the user's email address.

```python
class contactForm(forms.Form):
    name=forms.CharField(label="User Name",initial="Nihad",help_text="must be at least 10 characters",required=True,disabled=False)
    file=forms.FileField()

```

## HTML Form

The form is rendered using HTML and includes CSRF protection. It utilizes the `crispy` template tag to improve the form's presentation.

```html
{% load crispy_forms_tags%}
<form method="POST" style="width: 50%; height: 500px; margin: auto;" class="pt-5" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form | crispy }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

The form fields are displayed with labels, and a submit button is provided for user interaction.

## Form Processing

To handle form submissions, a view function `contactForm` is defined in Python. This function takes a `request` object, processes the form data, and renders the 'contact.html' template.

```python
def contactForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            f_file = form.cleaned_data['file']
            with open('./my_app/upload/' + f_file.name, 'wb+') as destination:
                for chunk in f_file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'my_app/contact.html', context={'form': form})
    else:
        form = contactForm()
    return render(request, 'my_app/contact.html', context={'form': form})
```


# Form Validataion 

This README provides information about a Django-based form API for building and processing user input.

## Form Definition

To create a form, a Django `contactForm` class is defined in Python. This form consists of two fields: `name` for the user's name and `email` for the user's email address.

```python
from django.core import validators
class studentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
# approach 1
    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")
        return valname
    def clean_email(self):
        valemail = self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("not correct convension .com format")
        return valemail
# Aproach 2
    def clean(self):
        cleaned_data = super().clean()  # Call the parent class clean() to get the cleaned data
        valname = cleaned_data['name']
        valemail = cleaned_data['email']

        if valname and len(valname) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")

        if valemail and '.com' not in valemail:
            raise forms.ValidationError("Not the correct '.com' email format")

        return cleaned_data  # Always return the cleaned data at the end of the clean() method
# Aproach 3
        name = forms.CharField(validators=[validators.MaxLengthValidator(45,message="max length must be 45 characters"),validators.MinLengthValidator(5,message="Atleast 5 char")])
        email = forms.EmailField(validators=[validators.EmailValidator(message="Please enter a valid email address")])
        age=forms.IntegerField(validators=[validators.MaxValueValidator(28,message="max value must be 28 "),validators.MinValueValidator(25,message="atleast 25 ")])
        file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="only pf files are allowed")])

        custom_name=forms.CharField(validators=[custom_name_func])
# Aproach 4 Custom Validation Make
    def len_check(value):
        if len(value) < 10:
            raise forms.ValidationError("Please enter atleast 10 characters")
    name = forms.CharField(validators=[len_check])


```

## HTML Form

The form is rendered using HTML and includes CSRF protection. It utilizes the `crispy` template tag to improve the form's presentation.

```html
{% load crispy_forms_tags%}
    <form method="POST" style="width: 50%; height: 500px; margin: auto;" class="pt-5">
        {% csrf_token %}
        {{form | crispy }}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
```

The form fields are displayed with labels, and a submit button is provided for user interaction.

## Form Processing

To handle form submissions, a view function `contactForm` is defined in Python. This function takes a `request` object, processes the form data, and renders the 'contact.html' template.

```python
def student_data(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/validateForm.html', context={'form': form})
    else:
        form = studentForm()
    return render(request, 'my_app/validateForm.html', context={'form': form})
```


# Very Normal inefficient password mathchig validation Form Validataion 

This README provides information about a Django-based form API for building and processing user input.

## Form Definition

To create a form, a Django `contactForm` class is defined in Python. This form consists of two fields: `name` for the user's name and `email` for the user's email address.

```python
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


```

## HTML Form

The form is rendered using HTML and includes CSRF protection. It utilizes the `crispy` template tag to improve the form's presentation.

```html
{% load crispy_forms_tags%}
    <form method="POST" style="width: 50%; height: 500px; margin: auto;" class="pt-5">
        {% csrf_token %}
        {{form | crispy }}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
```

The form fields are displayed with labels, and a submit button is provided for user interaction.

## Form Processing

To handle form submissions, a view function `contactForm` is defined in Python. This function takes a `request` object, processes the form data, and renders the 'contact.html' template.

```python
def password(request):
    if request.method == 'POST':
        form = password_validation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'my_app/passwordvalidation.html', context={'form': form})
    else:
        form = password_validation()
    return render(request, 'my_app/passwordvalidation.html', context={'form': form})
```



















