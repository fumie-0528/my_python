from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('register', views.register),
path('welcome', views.welcome),
path('login', views.login),
path('add_book', views.add_book),
path('book_detail/<int:id>', views.book_detail),
path('book_edit/<int:id>', views.book_edit),
path('book_update/<int:id>', views.book_update),
path('book_delete/<int:id>', views.book_delete),
path('logout', views.logout),
path('add_to_favorite/<int:id>', views.add_to_favorite),
path('un_favorite/<int:id', views.un_favorite)
]
