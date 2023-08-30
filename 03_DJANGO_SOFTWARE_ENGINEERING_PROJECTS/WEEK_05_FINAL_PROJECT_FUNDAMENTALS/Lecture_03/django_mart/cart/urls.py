from django.urls import path
from cart.views import cart,added_to_cart,remove_to_cart
urlpatterns = [
    path('', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', added_to_cart, name='add_to_cart'),
    path('remove_to_cart/<int:product_id>/', remove_to_cart, name='remove_to_cart'),
    path('delete_cart/<int:product_id>/', remove_to_cart, name='delete_cart'),
]

