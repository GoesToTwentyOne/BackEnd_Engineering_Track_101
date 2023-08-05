from django import forms
from book_app.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model =BookStoreModel
        fields= ['id','book_name','author','catagory']
    
