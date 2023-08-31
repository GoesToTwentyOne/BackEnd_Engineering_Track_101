from django.shortcuts import render,redirect
from store.models import Product
from cart.models import Cart,CartItem

# Create your views here.
def get_session_create(request):
    if not request.session.session_key:
        request.session.create()
        return request.session.session_key
def cart(request):
    cart_items=None
    total_amount=0
    tax_amount=0
    grand_total=0
    if request.user.is_authenticated:
            cart_items=CartItem.objects.filter(user=request.user)
            for item in cart_items:
                total_amount += (item.product.price*item.quantity)
        
    else:
        session_id=get_session_create(request)
        # cartid=Cart.objects.get(cart_id=session_id)
        cart_id=Cart.objects.get(cart_id=session_id)
        # cart_id=Cart.objects.filter(cart_id=session_id).exists()
        if cart_id:
            # cart_item=CartItem.objects.filter(cart=cartid)
            cart_items=CartItem.objects.filter(cart=cart_id)
            for item in cart_items:
                total_amount += (item.product.price*item.quantity)
        tax_amount=(2*total_amount)/100
        grand_total += (total_amount+tax_amount)
        
    return render(request, 'cart/cart.html',context={'cart_items':cart_items,'grand_total':grand_total,'tax':tax_amount,'total_amount':total_amount})


        
def added_to_cart(request, product_id):
    product=Product.objects.get(id=product_id)
    session_id=get_session_create(request)
    if request.user.is_authenticated:
        cart_item=CartItem.objects.filter(product=product,user=request.user).exists()
        if cart_item:
            item=CartItem.objects.get(product=product)
            item.quantity+=1
            item.save()
        else:
            cart_id=Cart.objects.get(cart_id=session_id)
            # cart_id=Cart.objects.filter(cart_id=session_id).exists()
            item=CartItem.objects.create(
                product=product,
                cart=cart_id,
                quantity=1,
                user=request.user,
            )
            item.save()
    else:
        cart_id=Cart.objects.filter(cart_id=session_id).exists()
        if cart_id:
            cart_item=CartItem.objects.filter(product=product).exists()
            if cart_item:
                item=CartItem.objects.get(product=product,cart=cart_id)
                item.quantity+=1
                item.save()
            else:
                cart_id=Cart.objects.get(cart_id=session_id)
                item=CartItem.objects.create(
                    cart=cart_id,
                    product=product,
                    quantity=1
                )
                item.save()
        else:
            cart=Cart.objects.create(cart_id=session_id)
            cart.save()
    
    return redirect('cart')

def remove_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    session_id=get_session_create(request)
    cart_id=Cart.objects.get(cart_id=session_id)
    if cart_id:
        cart_item=CartItem.objects.get(cart=cart_id,product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -=1
            cart_item.save()
        else:
            cart_item.delete()
    else:
        pass
    print(cart_item)
    return redirect('cart')
def delete_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    session_id=get_session_create(request)
    cart_id=Cart.objects.get(cart_id=session_id)
    if cart_id:
        cart_item=CartItem.objects.get(cart=cart_id,product=product)
        cart_item.delete()
    else:
        pass
    print(cart_item)
    return redirect('cart')