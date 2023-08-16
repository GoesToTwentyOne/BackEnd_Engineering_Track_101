from django.shortcuts import render
from my_app.paginations import ProductPagination,ProductLimitOffsetPagination,ProductCursorPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from my_app.models import Product,ProductReview
from rest_framework.permissions import IsAuthenticated
from my_app.serilizers import ProductSerializer,ProductReviewSerializer
from my_app.permissions import AdminorReadOnly,ReviewerOrReadOnly
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AdminorReadOnly]   #custom permission classes
    #searching
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    #ordering
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']
    pagination_class=ProductPagination
    #pagination_class=ProductLimitOffsetPagination
    # pagination_class=ProductCursorPagination
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [ReviewerOrReadOnly]   #custom permission classes
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username']
    filterset_fields = ['rating', 'product']
    # def get_queryset(self):
    #     queryset = ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset