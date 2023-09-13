# Build in genetic Class Based View
https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/

## TemplateView

```python
#TemplateView
from django.views.generic import TemplateView
# function based template  view
def home(request):
    return render(request, 'base.html')

# class based template view view
class HomeView(TemplateView):
    template_name='base.html'
     def get_context_data(self,**kwargs):
         context=super().get_context_data(**kwargs)
         context={'name':"Nihad Hossain",'age':23}
         print(context)
         print(kwargs)
         context.update(kwargs)   #dictionary updated
         print(context)
         return context
```
```python
#url
    path('',views.home,name='homepage'),
    path('',views.HomeView.as_view(),name='homepage'),
```


## ListView
```python
from django.views.generic import TemplateView,ListView,DetailView
# function book show view
def bookshow(request):
    book=BookStoreModel.objects.all()
    return render(request,'show_book.html',context={'book':book})

# class book show | LISTVIEW
class BookShow(ListView):
    model=BookStoreModel
    template_name='show_book.html'
    context_object_name='book'
    ordering=['id']

class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'details_show_book.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(id='1')#query 
    
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #query sorting author
    #     context= super().get_context_data(**kwargs)
    #     context={'book': BookStoreModel.objects.filter(author='nihadgo')}
    #     return context

    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #query sorting author
    #     context= super().get_context_data(**kwargs)
    #     context={'book': BookStoreModel.objects.all().order_by('id')}
    #     return context
```
```python
#url
    path('show_books/',views.bookshow,name='show'),
    path('book_store_show/',views.BookShow.as_view(),name='show'),

```
## Details View
```python
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'details_show_book.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(id='1')#query 
    
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #query sorting author
    #     context= super().get_context_data(**kwargs)
    #     context={'book': BookStoreModel.objects.filter(author='nihadgo')}
    #     return context

    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: #query sorting author
    #     context= super().get_context_data(**kwargs)
    #     context={'book': BookStoreModel.objects.all().order_by('id')}
    #     return context
```
```python
#url
   path('book_store_details/<int:id>',views.BookDetailsView.as_view(),name='details'),
```
```python
{% extends 'base.html' %}
{% block content %}
<div style="width: 50%; height: 500px; margin: auto;">
    <h1 style="text-align: center">Your Book List </h1>
    {% if book %}
    <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Book Name</th>
          </tr>
        </thead>
        <tbody>
            {% for item in book %}
          <tr>
            <td>{{item.id}}</td>
            <td><a href="{% url 'details' id=item.id %}">{{item.book_name}}</a></td>
          </tr>
          {% endfor %}
         
        </tbody>
      </table>
      {% else %}
      <h1 style="text-align: center">Your Book List Empty</h1>
      {% endif %}
</div>
```

```python
{% endblock %}
{% extends 'base.html' %}
{% block content %}
<div style="width: 78%; height: 500px; margin: auto;">
    <h1 style="text-align: center">Your Book Details </h1>
    <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Book Name</th>
            <th scope="col">Author </th>
            <th scope="col">Catagory</th>
            <th scope="col">Published Date</th>
            <th scope="col">Last Update</th>
            <th scope="col">ISBN</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{item.id}}</td>
            <td>{{item.book_name}}</td>
            <td>{{item.author}}</td>
            <td>{{item.catagory}}</td>
            <td>{{ item.first_published}}</td>
            <td>{{item.last_updated}}</td>
            <td>{{ item.isbn}}</td>
            <td><a href="{% url 'edit' pk=item.id %}" type="button" class="btn btn-danger btn-sm">Edit</a> <a href="{% url 'delete' pk=item.id %}" type="button" class="btn btn-warning btn-sm">Delete</a></td>
          </tr>
        </tbody>
      </table>
</div>

{% endblock %}

```

## Form View | Create 
```python
 #function book store form view
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
#Procdure 1
# class book store form view  
class BookFormView(FormView):
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show')
    def form_valid(self, form):
        print(form.cleaned_data)
        form.save(commit=True)
        return  redirect('show')


```
## Create View
```python
#Procdure 2
class BookFormView(CreateView):
    model = BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show')
```

## Update View
```python
# fucntion bookstore update view    
def edit(request,id):
    book=BookStoreModel.objects.get(pk=id)
    form=BookStoreForm(instance=book)
    if request.method == 'POST':
        form=BookStoreForm(request.POST,instance=book)
        if form.is_valid():
            form.save(commit=True)
            return redirect('show')
    return render(request,'store_book.html',context={'form':form})

# class bookstore update view    
class BookUpdateView(UpdateView):
    model=BookStoreModel
    form_class=BookStoreForm
    template_name='store_book.html'
    success_url=reverse_lazy('show')
```
```python
    <td><a href="{% url 'edit' pk=item.id %}" type="button" class="btn btn-danger btn-sm">Edit</a> <a href="{% url 'delete' pk=item.id %}" type="button" class="btn btn-warning btn-sm">Delete</a></td>
    # path('edit_book/<int:id>',views.edit,name="edit"),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view(),name="edit"),
```
## Delete View
```python
# fucntion book store delete view    
def delete(request,id):
    book=BookStoreModel.objects.get(pk=id)
    book.delete()
    return redirect('show')

#class bookstore delete view
class BookDeleteView(DeleteView):
    model=BookStoreModel
    template_name='confirmation.html'
    success_url=reverse_lazy('show')
```

```python
    #url
    <td><a href="{% url 'edit' pk=item.id %}" type="button" class="btn btn-danger btn-sm">Edit</a> <a href="{% url 'delete' pk=item.id %}" type="button" class="btn btn-warning btn-sm">Delete</a></td>
    # path('delete_book/<int:id>',views.delete,name="delete"),
    path('delete_book/<int:pk>',views.BookDeleteView.as_view(),name="delete"),
```

# Cookies

## set Cookies
```python
def home(request):
    response = render(request,'home.html')
    response.set_cookie('name','alex',max_age=30)
    response.set_cookie('name','alex',expires=datetime.utcnow()+timedelta(days=10))
    return response
```
## get Cookies
```python
def get_cookies(request):
    name=request.COOKIES.get('name')
    return render(request,'get_cookies.html',context={'name':name})
```

## delete Cookies
```python
def delete_cookies(request):
    response=render(request,'delete_cookies.html')
    response.delete_cookie('name')
    return response
```
## set Sessions 
```python
def set_session(request):
    data = {
        'name': 'alex',
        'age': 18,
        'year': 2023,
    }
    # Update the session with the provided data
    request.session.update(data)
    # Save the session data
    request.session.save()
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date() )
    return render(request, 'set_session.html')
```
## get Sessions 
```python
def get_sessions(request):
    name=request.session.get('name')
    age=request.session.get('age')
    year=request.session.get('year')
    return render(request,'get_sessions.html',context={'name':name, 'age':age, 'year':year})
```
## delete session
```python
def delete_session(request):
    # del request.session['name']
    # request.session.clear_expired()
    request.session.flush()
    return render(request,'delete_session.html')

```
## modified session
```python
def session_expired(request):
    if 'name' in request.session:
        name=request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'session_running.html')
    else:
        return HttpResponse("Your session expired")

```
```python
SESSION_COOKIE_AGE=10
```
