from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet,basename="books")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # METHOD 1 API VIEW
    # path('books/',views.BookListView.as_view(), name="bookstore"), #get /post
    # path('books/<int:pk>/',views.BookListViewUpdateDelete.as_view(), name="bookstore"), #update Delete
    
    # METHOD 2 Generic VIEW
    # path('books/',views.BookListCreateAPIView.as_view(), name="bookstore"), #get /post
    # path('books/<int:pk>/',views.BookRetrieveUpdateDestroyAPIView.as_view(), name="bookstore") #update Delete
    
    # METHOD 3
    path('', include(router.urls)),
]