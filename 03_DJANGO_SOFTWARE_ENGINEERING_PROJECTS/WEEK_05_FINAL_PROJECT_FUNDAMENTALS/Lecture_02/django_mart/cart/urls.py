from django.urls import path
from cart.views import cart,added_to_cart
urlpatterns = [
    path('', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', added_to_cart, name='add_to_cart')
]

