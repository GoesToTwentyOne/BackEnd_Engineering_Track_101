from django.shortcuts import render
from cart.models import Cart,CartItem


# Create your views here.
def order_complete(request):
    return render(request, 'orders/order_complete.html')


def place_order(request):
    print(request.POST)
    cart_items=None
    total_amount=0
    tax_amount=0
    grand_total=0
    cart_items=CartItem.objects.filter(user=request.user)
    for item in cart_items:
        for item in cart_items:
            total_amount += (item.product.price*item.quantity)
    tax_amount=(2*total_amount)/100
    grand_total += (total_amount+tax_amount)
    return render(request, 'orders/place-order.html',context={'cart_items':cart_items,'grand_total':grand_total,'tax':tax_amount,'total_amount':total_amount})