# REST Framework

# Serializer Setup
```python
#model 
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    CATEGORY = (
    ('Mystery', 'Mystery'),
    ('Thriller', 'Thriller'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Humor', 'Humor'),
    ('Horror', 'Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True) 
    last_pub = models.DateTimeField(auto_now=True) 
```
```python
#serializer  setup
from rest_framework import serializers
from api.models import BookStoreModel
class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookStoreModel
        fields='__all__'
    
```
# Get Post Update DELETE
```python
from django.shortcuts import render
from api.models import BookStoreModel
from api.serializers import BookStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
# METHODS 1 API VIEW


class BookListView(APIView):

    def get(self, request, format=None):
        model = BookStoreModel.objects.all()
        serializer = BookStoreSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookListViewUpdateDelete(APIView):

    Retrieve, update or delete a snippet instance.

    def get_object(self, pk):
        try:
            return BookStoreModel.objects.get(pk=pk)
        except BookStoreModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookStoreSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookStoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# METHODS 2 Generic VIEW



class BookListCreateAPIView(generics.ListCreateAPIView): #get | post
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): #READ  UPDATE DELETE 
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    

# METHODS 3  VIEWSET
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
```
```python
# router set
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
```