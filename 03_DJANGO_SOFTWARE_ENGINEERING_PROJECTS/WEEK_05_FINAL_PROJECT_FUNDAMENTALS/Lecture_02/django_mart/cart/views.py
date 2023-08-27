from django.shortcuts import render,redirect
from store.models import Product
from cart.models import Cart,CartItem

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')


def added_to_cart(request, product_id):
    product=Product.objects.get(id=product_id)
    
    session_id=request.session.session_key
    cart_id=Cart.objects.filter(cart_id=session_id).exists()
    if cart_id:
        cart_item=CartItem.objects.filter(product=product).exists()
        if cart_item:
            item=CartItem.objects.get(product=product)
            item.quantity+=1
            item.save()
        else:
            cart_id=Cart.objects.get(cart_id=session_id)
            item=CartItem.objects.create(
                product=product,
                cart=cart_id,
                quantity=1
            )
            item.save()
    else:
        cart=Cart.objects.create(cart_id=session_id)
        cart.save()
    
    return redirect('cart')