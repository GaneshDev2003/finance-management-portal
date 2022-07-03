from django.db import models
from apps.bank_account.models import BankAccount
# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=50)
    f_name  = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    password = models.CharField(max_length = 50)
    accounts = models.ManyToManyField(BankAccount)

