from django.contrib import admin
from accounts.models import UserBankAccountModel
from accounts.models import UserAddressModel
# Register your models here.
admin.site.register(UserBankAccountModel)
admin.site.register(UserAddressModel)
