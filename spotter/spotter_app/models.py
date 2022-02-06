from django.db import models
from sqlalchemy import ForeignKey
from django.contrib import messages
class UserManager(models.Manager):
    def basic_validator(self,post_data):
        errors = {}
        if len(post_data["username_input"]) >15:
            errors["username_input"] = "Username Input should be 15 characters or less"
        elif len(post_data["username_input"]) <2:
            errors["username_input"] = "Username Input should be longer than 1 character"    
        return errors

class User(models.Model):
    objects = UserManager()
    username = models.CharField(max_length = 15)
    name = models.TextField()
    bio = models.TextField()
    password = models.TextField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User,related_name="post_author",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    reps = models.IntegerField(default=0)

class Comments(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User,related_name="comment_author",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    reps = models.IntegerField(default=0)


# Create your models here.
# User {
#   - posts (one to many) posts = models.ForeignKey(User, related_name=, on_delete=models.CASCADE)
#   - comments (one to many)
#   - username
#   - name
#   - bio
#   - password
#   - created
#   - updated
# }

# Post {
#     title
#     content
#     author (foreign key -> User) author = models.(foreign_key=, related_name=)
#     created
#     updated = models.DateTimeField(auto_now=True)
#     comments (one to many)
#     reps
# }

# Comment {
#     content
#     author (foreign key -> User)
#     created
#     updated = models.DateTimeField(auto_now=True)
#     reps
# }

