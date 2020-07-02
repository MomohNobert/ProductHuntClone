from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

signUpPage = 'user/signup.html'


def signup(request):
    if request.method == 'POST':
        # The user wants to sign up!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, signUpPage, {'error': 'Username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                print("Done! Created new user")
                return redirect('home')
        else:
            return render(request, signUpPage, {'error': 'Passwords do not match!'})
    else:
        # User wants to enter info!
        return render(request, signUpPage)


def login(request):
    return render(request, 'user/login.html')


def logout(request):
    # TODO Need to route to homepage
    # don't forget logout
    return render(request, signUpPage)
