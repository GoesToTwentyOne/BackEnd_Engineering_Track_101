from django.contrib import admin
from book_app.models import BookStoreModel
# Register your models here.
#admin.site.register(BookStoreModel)

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'catagory', 'first_published', 'last_updated', 'isbn')
admin.site.register(BookStoreModel,BookStoreModelAdmin)