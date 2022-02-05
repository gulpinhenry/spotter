from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    test_arr = ['<div class="test" message="# ' + str(i) + ' generated with Django templates!"></div>' for i in range(1, 4)]
    context = {
        'test': test_arr,
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def user(request, username):
    context = {
        'username': username,
    }
    return render(request, 'user.html', context)