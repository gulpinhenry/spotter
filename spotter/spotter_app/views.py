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
    group_obj = Group.objects.filter(name=group_name)
    if len(group_obj) <= 0:
        return redirect("/")
    group_obj = group_obj[0]
    posts_obj = group_obj.post_group.all()
    posts = []
    for post in posts_obj:
        post_context = {
            "id": post.id,
            "author": post.author,
            "post": f'<div class="post" title={post.title} content="{post.content}" author="{post.author.name}" created="{post.created}"></div>',
            "comments": [],
        }
        for comment in post.post_comments.all():
            post_context["comments"].append(
                {
                    "id": comment.id,
                    "content": f'<div class="comment" content="{comment.content}" author="{comment.author.name}" created="{comment.created}"></div>',
                })
        posts.append(post_context)
    context = {
        "posts": posts,
        "group_name": group_obj.name,
    }
    return render(request, 'group.html', context)

def post_to_group(request, group_name):
    if request.method == "POST":
        group_obj = Group.objects.filter(name=group_name)
        if len(group_obj) <= 0:
            return redirect("/")
        group_obj = group_obj[0]
        user = User.objects.filter(id=request.session['user_id'])
        if len(user) <= 0:
            return redirect("/")
        user = user[0]
        Post.objects.create(title=request.POST["title_input"], content=request.POST["content_input"], author=user, group=group_obj)
        return redirect(f"/group/{group_name}")
    return redirect("/")

def reply_to_post(request, group_name, post_id):
    if request.method == "POST":
        group_obj = Group.objects.filter(name=group_name)
        if len(group_obj) <= 0:
            return redirect("/")
        group_obj = group_obj[0]
        user = User.objects.filter(id=request.session['user_id'])
        if len(user) <= 0:
            return redirect("/")
        user = user[0]
        post_obj = Post.objects.filter(id=post_id)
        if len(post_obj) <= 0:
            return redirect("/")
        post_obj = post_obj[0]
        Comment.objects.create(content=str(f"@{post_obj.author.name} " + request.POST["reply_input"]), author=user, parent_post=post_obj)
        return redirect(f"/group/{group_name}")
    return redirect("/")

def reply_to_comment(request, group_name, post_id, comment_id):
    if request.method == "POST":
        group_obj = Group.objects.filter(name=group_name)
        if len(group_obj) <= 0:
            return redirect("/")
        group_obj = group_obj[0]
        user = User.objects.filter(id=request.session['user_id'])
        if len(user) <= 0:
            return redirect("/")
        user = user[0]
        post_obj = Post.objects.filter(id=post_id)
        if len(post_obj) <= 0:
            return redirect("/")
        post_obj = post_obj[0]
        comment_obj = Comment.objects.filter(id=comment_id)
        if len(comment_obj) <= 0:
            return redirect("/")
        comment_obj = comment_obj[0]
        Comment.objects.create(content=str(f"@{comment_obj.author.name} " + request.POST["reply_input"]), author=user, parent_post=post_obj)
        return redirect(f"/group/{group_name}")
    return redirect("/")
    