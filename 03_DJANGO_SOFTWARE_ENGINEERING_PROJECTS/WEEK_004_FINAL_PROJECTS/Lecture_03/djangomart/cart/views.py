from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id) #get the product
    # If the user is authenticated
    if current_user.is_authenticated:
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_items = CartItem.objects.filter(product=product, user=current_user)
            print(cart_items)
            item = CartItem.objects.get(product=product, user=current_user)
            item.quantity += 1
            item.save()
            
        else:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id = _cart_id(request)
                )
            cart.save()
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
                user = current_user
            )
            cart_item.save()
        return redirect('cart')
    else:
        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
            cart.save()
        
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity  += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cart,
                )
            cart.save()
    return redirect('cart')
