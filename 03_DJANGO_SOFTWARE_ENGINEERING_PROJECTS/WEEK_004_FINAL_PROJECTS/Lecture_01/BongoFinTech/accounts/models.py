from django.db import models
from django.contrib.auth.models import User
from accounts.constants import ACCOUNT_TYPE, GENDER_TYPE

class UserBankAccountModel(models.Model):
    user = models.OneToOneField(User, related_name='bank_account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=15, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Name: {self.user.username} ------ Account No: {self.account_no}"

class UserAddressModel(models.Model):
    user = models.OneToOneField(User, related_name="address", on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Name: {self.user.username}------- Email: {self.user.email}"
