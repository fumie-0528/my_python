# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('blue', views.create),
    path('blog', views.blog),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('delete', views.destroy),
]