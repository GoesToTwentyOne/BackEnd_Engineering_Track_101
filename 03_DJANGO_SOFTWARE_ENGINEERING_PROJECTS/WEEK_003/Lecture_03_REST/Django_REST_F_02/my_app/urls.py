from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product', views.ProductViewSet,basename="product")
router.register(r'productreview', views.ProductReviewViewSet,basename="productreview")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include("rest_framework.urls")),
]