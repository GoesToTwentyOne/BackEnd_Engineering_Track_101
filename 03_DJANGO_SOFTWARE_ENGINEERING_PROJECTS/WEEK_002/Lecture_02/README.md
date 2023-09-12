# CRUD APP: BOOK STORE

This README.md file provides an overview of a Django CRUD (Create, Read, Update, Delete) application for a book store, including the relevant model, forms, and operations.

## Book Store Model
The `BookStoreModel` represents the structure of book records in the database. It includes fields for book name, author, category, publication date, and ISBN number.

## Book Store Model
```python
import random
def create_new_ref_number():
        return random.randint(0, 9999)
class BookStoreModel(models.Model):
    CATEGORY_CHOICES = [
        ('western', 'Western'),
        ('revenge', 'Revenge'),
        ('spaghetti_western', 'Spaghetti Western'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('historical', 'Historical'),
        ('adventure', 'Adventure'),
        ('crime', 'Crime'),
        ('thriller', 'Thriller'),
        ('noir', 'Noir'),
        ('romance', 'Romance'),
        ('neo_western', 'Neo-Western'),
        ('martial_arts', 'Martial Arts'),
        ('ensemble_cast', 'Ensemble Cast'),
        ('fantasy', 'Fantasy'),
        ('comedy', 'Comedy'),
        ('redemption', 'Redemption'),
        ('classic', 'Classic'),
        ('biographical', 'Biographical'),
        ('tragedy', 'Tragedy'),
    ]
    id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=40)
    catagory=models.CharField(max_length=75,choices=CATEGORY_CHOICES)
    first_published=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True,)
    isbn = models.CharField(
           max_length = 75,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number
      )
```


## Book Store Model FORM
The `BookStoreForm` is a Django form class generated from the `BookStoreModel` for creating and editing book records.

```python
from django import forms
from book_app.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model =BookStoreModel
        fields= ['id','book_name','author','catagory']
```
## Register Model
The `BookStoreModel` is registered with the Django admin interface to enable easy management of book records.

```python
class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'catagory', 'first_published', 'last_updated', 'isbn')
admin.site.register(BookStoreModel,BookStoreModelAdmin)
```
## CRUD Operations
### Create Operation
The `storeBook` view function allows users to create new book records by submitting a form.

```python
def storeBook(request):
    if request.method == 'POST':
        book=BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            print(book.cleaned_data)
            return redirect('show')
    else:
        book=BookStoreForm()
    return render(request,'store_book.html',context={'form':book})

```
### Read Opearation
The `bookshow` view function retrieves and displays a list of all book records.

```python
def bookshow(request):
    book=BookStoreModel.objects.all()
    return render(request,'show_book.html',context={'book':book})

```
### Edit/Update Opearation
The `edit` view function allows users to edit and update existing book records.

```python
def edit(request,id):
    book=BookStoreModel.objects.get(pk=id)
    form=BookStoreForm(instance=book)
    if request.method == 'POST':
        form=BookStoreForm(request.POST,instance=book)
        if form.is_valid():
            form.save(commit=True)
            return redirect('show')
    return render(request,'store_book.html',context={'form':form})
#URL:
path('edit_book/<int:id>',views.edit,name="edit"),
#Link
<a href="{% url 'edit' id=item.id %}" type="button" class="btn btn-danger btn-sm">Edit</a>

```
### Delete Opearation
The `delete` view function allows users to delete book records

```python
def delete(request,id):
    book=BookStoreModel.objects.get(pk=id)
    book.delete()
    return redirect('show')
#URL:
path('delete_book/<int:id>',views.delete,name="delete")
#Link
<a href="{% url 'delete' id=item.id %}" type="button" class="btn btn-warning btn-sm">Delete</a>
```

This Django CRUD application for a book store enables users to perform essential operations on book records, including creation, reading, updating, and deletion. The provided code snippets represent the core functionality of the application. You can integrate them into your Django project as needed.