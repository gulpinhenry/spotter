from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index), # dashboard/feed
    path('login', views.login), # login returning user
    path('register', views.register), # register new user
    path('user/<str:username>', views.user), # view user profile
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)