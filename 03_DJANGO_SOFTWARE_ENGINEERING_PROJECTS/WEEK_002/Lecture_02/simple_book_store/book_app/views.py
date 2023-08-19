from django.shortcuts import render,redirect
from book_app.forms import BookStoreForm
from book_app.models import BookStoreModel

# Create your views here.
def home(request):
    return render(request, 'base.html')



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

def bookshow(request):
    book=BookStoreModel.objects.all()
    return render(request,'show_book.html',context={'book':book})

def edit(request,id):
    book=BookStoreModel.objects.get(pk=id)
    form=BookStoreForm(instance=book)
    if request.method == 'POST':
        form=BookStoreForm(request.POST,instance=book)
        if form.is_valid():
            form.save(commit=True)
            return redirect('show')
    return render(request,'store_book.html',context={'form':form})


def delete(request,id):
    book=BookStoreModel.objects.get(pk=id)
    book.delete()
    return redirect('show')