from django.contrib import admin
from cart.models import Cart,CartItem
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=['cart_id','cart_name']
    prepopulated_fields={'cart_name':('cart_id',)}
admin.site.register(Cart,CartAdmin)
class CartItemAdmin(admin.ModelAdmin):
    list_display=['product','cart','quantity','is_active']
admin.site.register(CartItem,CartItemAdmin)
