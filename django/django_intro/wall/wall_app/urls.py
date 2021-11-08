from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('register', views.register),
path('login', views.login),
path('logout', views.logout),
path('welcome', views.welcome),
path('message', views.message),
path('post_message', views.post_message),
path('post_comment/<int:id>', views.post_comment),
path('delete_comment/<int:id>', views.delete_comment)
]