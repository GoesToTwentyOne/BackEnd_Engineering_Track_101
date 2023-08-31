from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=120)
    status=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Accected','Accected'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_number=models.CharField(max_length=100)
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=52)
    address_line1=models.CharField(max_length=100)
    address_line2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    order_note=models.TextField(max_length=200)
    order_total=models.FloatField()
    tax=models.FloatField()
    status=models.CharField(max_length=150,choices=STATUS)
    ip=models.CharField(max_length=100,blank=True,null=True)
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class OrderProduct(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
