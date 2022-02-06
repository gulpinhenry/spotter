from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import *
import bcrypt
# Create your views here.


def index(request):
    test_arr = ['<div class="test" message="# ' +
                str(i) + ' generated with Django templates!"></div>' for i in range(1, 4)]
    context = {
        'test': test_arr,
    }
    return render(request, 'index.html', context)


def login(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST['username_input'])
        if len(user) <= 0:
            messages.error(request, "Incorrect username or password.")
            return redirect("/login")
        if bcrypt.checkpw(request.POST['password_input'].encode(), user[0].password.encode()):
            request.session['user_id'] = user.id
            return redirect("/")
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect("/login")
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        user = User.objects.filter(username=request.POST['username_input'])
        if len(user) > 0:
            messages.error(request, "Username already taken.")
            return redirect("/register")
        pw_hash = bcrypt.hashpw(
            request.POST["password_input"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            username=request.POST["username_input"], password=pw_hash)
        request.session['user_id'] = user.id
    return render(request, 'register.html')


def user(request, username):
    user_obj = User.objects.filter(username=username)
    if len(user_obj) <= 0:
        return redirect("/")
    context = {
        'username': username,
        'name': user_obj[0].name,
        'bio': user_obj[0].bio,
        'groups': user_obj[0].joined_groups.all,
        'posts': user_obj[0].post_author.all,
    }
    return render(request, 'user.html', context)

def edit(request, username):
    context = {
        'username': username,
    }
    if request.method == "POST":
        print("hello")
        user = User.objects.filter(username=username)
        if len(user) <= 0:
            return redirect("/")
        user_obj = user[0]
        user_obj.name = request.POST["name_input"]
        user_obj.bio = request.POST["bio_input"]
        user_obj.save()
        request.session['user_id'] 
        return redirect("/user/" + username)
    return render(request, 'edit.html', context)

def group(request, group_name):
    return HTTPResponse("pog")
