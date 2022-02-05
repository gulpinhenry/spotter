from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.

class Person(models.Model):
    id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40, blank=False)
    slug = slug = models.SlugField(max_length=400, unique=True, blank = True)
    bio = models.TextField()
    realname = models.CharField(max_length=30, blank=True)
    #upvotes = models.IntegerField(default) ?? necessary?

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(Post, self).save(*args, **kwargs)

class Post(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length = 400)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.SET_NULL)
    timeCreated = models.TimeField(auto_now=True, auto_now_add=True)
    user = models.ForeignKey(Person, on_delete=models.SET_NULL)
    content = models.TextField()
    #reps = models.IntegerField()

class Reps(models.Model):
    id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.SET_NULL)

    
