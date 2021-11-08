from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    path('trips', views.trips),
    path('trips/new', views.new),
    path('trips/create', views.create),
    path('trips/detail/<int:id>', views.detail),
    
    path('trips/edit/<int:id>', views.edit),
    path('trips/update/<int:id>', views.update),
    path('trips/delete/<int:id>', views.delete), 

    path('trips/join/<int:id>', views.join),
    path('trips/cancel/<int:id>', views.cancel)
]