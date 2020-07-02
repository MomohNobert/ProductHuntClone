from django.shortcuts import render


# Create your views here.

def signup(request):
    return render(request, 'user/signup.html')


def login(request):
    return render(request, 'user/login.html')


def logout(request):
    # TODO Need to route to homepage
    # don't forget logout
    return render(request, 'user/signup.html')
