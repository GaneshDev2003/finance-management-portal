from django.db import models
import datetime

# Create your models here.

class Transaction(models.Model):
    transactionType = models.CharField(max_length=50)
    transactionAmount = models.FloatField()
    transactionPurpose = models.CharField(max_length= 150)
    transactionDate = models.DateField(default = datetime.date.today)
    class Meta :
        ordering = ('-transactionDate',)
class BankAccount(models.Model):
    accountNumber = models.CharField(max_length=50)
    balance = models.FloatField(null = True)
    accountType = models.CharField(max_length=50)
    transactions = models.ManyToManyField(Transaction)

