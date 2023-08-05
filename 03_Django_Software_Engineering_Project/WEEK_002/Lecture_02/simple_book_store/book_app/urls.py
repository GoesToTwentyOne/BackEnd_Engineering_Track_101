from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('book_store/',views.storeBook,name='store'),
    path('show_books/',views.bookshow,name='show'),
    path('edit_book/<int:id>',views.edit,name="edit"),
    path('delete_book/<int:id>',views.delete,name="delete")
]
