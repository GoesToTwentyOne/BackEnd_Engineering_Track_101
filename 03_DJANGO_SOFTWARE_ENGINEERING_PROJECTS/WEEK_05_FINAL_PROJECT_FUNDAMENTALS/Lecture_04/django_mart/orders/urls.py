from django.urls import path
from orders.views import order_complete,place_order

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_complete/', order_complete, name='order_complete')
    
]