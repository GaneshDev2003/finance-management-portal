from django.contrib import admin

from apps.bank_account.models import BankAccount, Transaction

# Register your models here.
admin.site.register(BankAccount)
admin.site.register(Transaction)