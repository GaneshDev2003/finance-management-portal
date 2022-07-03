from django.http import HttpResponse
from django.shortcuts import render,redirect
from apps.user_auth.models import UserModel
from .models import BankAccount, Transaction
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
# Create your views here.

def get_user(request):
    current_user = request.user
    user = UserModel.objects.get(username = current_user.username)
    return user
def get_monthly_transaction(transaction_list):
    today = datetime.datetime.now()
    monthly_transaction = transaction_list.filter(transactionDate__month = today.month)
    return monthly_transaction
def account_view(request):
    user = get_user(request)
    accounts = user.accounts;
    print(accounts)
    return render(request, 'accounts/accounts.html', context = {'accounts' : accounts})
def transaction_list_view(request, account_id):
    account = BankAccount.objects.get(pk = account_id)
    transaction_list = account.transactions.all()
    p = Paginator(transaction_list, 10)
    #page_number = 1
    page_number = request.GET.get('page')
    print('Page number :' ,page_number)
    page_obj = p.get_page(page_number)
    #print(page_obj)
    return render(request, 'accounts/transactionlist.html' , context = {'transactions' : page_obj}) 


def account_add_view(request):
    user = get_user(request)
    if(request.method=='POST'):
        print('added account')
        form_data = request.POST
        bank_account = BankAccount.objects.create(
            accountNumber = form_data['accountNumber'],
            accountType = form_data['accountType'],
            balance = form_data['balance'],
        )
        user.accounts.add(bank_account)
    #print('added account')
    return render(request, 'accounts/add_account.html' , context={})

def transaction_delete_view(request,account_id, transaction_id):
    if(request.method == 'POST'):
        print('deleting transaction')
        transaction = Transaction.objects.get(pk=transaction_id)
        account = BankAccount.objects.get(pk = account_id)
        if(transaction.transactionType == 'credit'):
            account.balance -= transaction.transactionAmount
        else :
            account.balance += transaction.transactionAmount
        transaction.delete()
        account.save()
        return HttpResponse(status = 204, headers = {'HX-Trigger' : 'transactionListChanged'})
    return render(request,'accounts/delete_transaction.html',context={})

def account_detail_view(request, account_id):
    account = BankAccount.objects.get(pk = account_id)
    transaction_list = account.transactions.all()
    monthly_transactions = transaction_list.filter()
    p = Paginator(transaction_list, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    monthly_transactions = get_monthly_transaction(transaction_list)
    monthly_expenditure = 0
    monthly_earning = 0
    for transaction in monthly_transactions:
        if(transaction.transactionType == 'debit'):
            monthly_expenditure+=transaction.transactionAmount
        else:
            monthly_earning+=transaction.transactionAmount
    
    monthly_earning = float("{:.2f}".format(monthly_earning))
    monthly_expenditure = float("{:.2f}".format(monthly_expenditure))
    account.balance = float("{:.2f}".format(account.balance))
    #print(type(monthly_earning))
    print(monthly_earning)
    round(account.balance,2)
    return render(request, 'accounts/account_details.html' , context = {
        'account' : account,
        'transactions' : page_obj,
        'earning': monthly_earning,
        'expenditure':monthly_expenditure,
    })
def transaction_update_view(request, account_id, transaction_id):
    transaction = Transaction.objects.get(pk = transaction_id)
    account = BankAccount.objects.get(pk = account_id)
    if(request.method == 'POST'):
        form_data = request.POST
        
        if(transaction.transactionType == 'credit'):
            account.balance -= transaction.transactionAmount
        else :
            account.balance += transaction.transactionAmount
        transaction.transactionAmount = form_data['transactionAmount']
        transaction.transactionPurpose = form_data['transactionPurpose']
        transaction.transactionDate = form_data['transactionDate']
        transaction.transactionType = form_data['transactionType']
        transaction.save()
        return HttpResponse(status = 204, headers = {'HX-Trigger' : 'transactionListChanged'})
    return render(request, 'accounts/update_transaction.html', context={'transaction' : transaction})
def transaction_add_view(request, account_id):
    account = BankAccount.objects.get(pk = account_id)
    if(request.method == 'POST'):
        form_data = request.POST
        transaction = Transaction.objects.create(
            transactionAmount= form_data['transactionAmount'],
            transactionType = form_data['transactionType'],
            transactionPurpose = form_data['transactionPurpose'],
            transactionDate = form_data['transactionDate']
        )
        account.transactions.add(transaction)
        print(transaction.transactionAmount)
        flip = 1
        if(transaction.transactionType == 'debit'):
            flip = -1
        account.balance += flip*float(transaction.transactionAmount)
        account.save()
        #print(account.balance)
        return HttpResponse(status = 204, headers = {'HX-Trigger' : 'transactionListChanged'})
    return render(request, 'accounts/add_transaction.html',context = {})