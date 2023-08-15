from django.shortcuts import render
from rest_framework import viewsets
from my_app.models import Product,ProductReview
from rest_framework.permissions import IsAuthenticated
from my_app.serilizers import ProductSerializer,ProductReviewSerializer
from my_app.permissions import AdminorReadOnly,ReviewerOrReadOnly
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AdminorReadOnly]   #custom permission classes
class ProductReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    permission_classes = [ReviewerOrReadOnly]   #custom permission classes
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer