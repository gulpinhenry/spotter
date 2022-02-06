from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index),  # dashboard/feed
    path('login', views.login),  # login returning user
    path('register', views.register),  # register new user
    path('user/<str:username>', views.user),  # view user profile
    path('user/<str:username>/edit', views.edit), # edit user profile
    path('group/new', views.create_group),  # create a group
    path('group/<str:group_name>', views.group),  # view a group
    path('group/<str:group_name>/users', views.group),  # view the users in a group
    path('group/<str:group_name>/post', views.post_to_group),  # view the users in a group
    path('group/<str:group_name>/reply/<int:post_id>', views.reply_to_post),  # reply to a post
    path('group/<str:group_name>/reply/<int:post_id>/<int:comment_id>', views.reply_to_comment),  # reply to a comment
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
