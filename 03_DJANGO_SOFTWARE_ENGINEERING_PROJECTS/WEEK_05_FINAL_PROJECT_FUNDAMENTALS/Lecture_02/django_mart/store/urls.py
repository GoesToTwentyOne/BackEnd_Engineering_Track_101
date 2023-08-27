from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:product_slug>/<slug:category_slug>/', views.product_detail, name='single_products'),
    
]