from django.db import models
from accounts.models import UserBankAccountModel
from transactions.constants import TRANSACTION_TYPE

# Create your models here.
class UserTransactionModel(models.Model):
    account=models.ForeignKey(UserBankAccountModel, related_name="bank_transactions",on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12, decimal_places=2,null=True)
    balance_after_transaction=models.DecimalField(max_digits=12,decimal_places=2,null=True)
    transaction_type=models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approved=models.BooleanField(default=False)
    class Meta:
        ordering = ['timestamp']