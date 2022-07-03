from django.shortcuts import render,redirect
from .models import UserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home_view(request):
    return render(request,'home.html',context={})

def sign_up_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        User.objects.create_user(
            username = username,
            first_name = f_name,
            last_name = l_name,
            password = request.POST['password'],
        )
        UserModel.objects.create(
            username = username,
            f_name = f_name,
            l_name = l_name,
        )
        return redirect('home')
    return render(request, 'auth/signup.html',context={})

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        print(username , password)
        user = authenticate(username = username, password = password)
        if(user is not None):
            login(request,user)
            print('Logged in successfully')
            return redirect('home')
        else:
            print("user not found")
    return render(request, 'auth/login.html', context={})

def logout_view(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('home')
    return render(request, 'auth/logout_request.html', context = {})
    
