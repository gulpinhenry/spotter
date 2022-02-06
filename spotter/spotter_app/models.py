from django.db import models

from django.contrib import messages


class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        try:
            if len(post_data["username_input"]) > 15:
                errors["username_input"] = "Username should be 15 characters long or less."
            elif len(post_data["username_input"]) < 2:
                errors["username_input"] = "Username should be at least 2 characters long."
            if len(post_data["password_input"]) < 8:
                errors["password_input"] = "Password should be at least 8 characters long."
        except:
            errors["unknown_error"] = "An unknown error has occured."
        return errors


class User(models.Model):
    objects = UserManager()
    username = models.CharField(max_length=15)
    name = models.TextField(default="Anonymous Gym Goer")
    bio = models.TextField(default="")
    password = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


class Group(models.Model):
    name = models.CharField(max_length=15)
    group_users = models.ManyToManyField(User, related_name="joined_groups")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(
        User, related_name="post_author", on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, related_name="post_group", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    reps = models.IntegerField(default=0)


class Comments(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User, related_name="comment_author", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    reps = models.IntegerField(default=0)
