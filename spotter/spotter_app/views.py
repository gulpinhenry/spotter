from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    test_arr = ['<div class="test" message="# ' + str(i) + ' generated with Django templates!"></div>' for i in range(1, 4)]
    context = {
        'test': test_arr,
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        User.objects.create(username = request.POST["username_input"], bio =  request.POST["bio_input"], name =  request.POST["realname_input"] )
        print("hahaha")

    return render(request, 'register.html')

def user(request, username):
    context = {
        'username': username,
    }
    return render(request, 'user.html', context)