from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home,name='homepage'),
    path('',views.HomeView.as_view(),name='homepage'),
    # path('book_store/',views.storeBook,name='store'),
    path('book_store/',views.BookFormView.as_view(),name='store'),
     # path('show_books/',views.bookshow,name='show'),
    path('book_store_show/',views.BookShow.as_view(),name='show'),
    path('book_store_details/<int:id>',views.BookDetailsView.as_view(),name='details'),
    # path('edit_book/<int:id>',views.edit,name="edit"),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view(),name="edit"),
    # path('delete_book/<int:id>',views.delete,name="delete"),
    path('delete_book/<int:pk>',views.BookDeleteView.as_view(),name="delete"),
    
]