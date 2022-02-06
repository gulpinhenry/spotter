from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index),  # dashboard/feed
    path('login', views.login),  # login returning user
    path('register', views.register),  # register new user
    path('user/<str:username>', views.user),  # view user profile
    path('group/<str:group_name>', views.group),  # view a group
    path('group/<str:group_name>/users', views.group),  # view the users in a group
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
