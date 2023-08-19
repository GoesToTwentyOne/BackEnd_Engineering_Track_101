from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from book_app.models import BookStoreModel
from book_app.forms import BookStoreForm
# Create your views here.


# function home view
def home(request):
    return render(request, 'base.html')

# class home view
class HomeView(TemplateView):
    template_name='base.html'
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context={'name':"Nihad Hossain",'age':23}
    #     print(context)
    #     print(kwargs)
    #     context.update(kwargs)   #dictionary updated
    #     print(context)
    #     return context
    
  
# function book store form view
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

#Procdure 2
# class BookFormView(CreateView):
#     model = BookStoreModel
#     template_name='store_book.html'
#     form_class=BookStoreForm
#     success_url=reverse_lazy('show')



# function book show view
def bookshow(request):
    book=BookStoreModel.objects.all()
    return render(request,'show_book.html',context={'book':book})

# class book show view   
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
