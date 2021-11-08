from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows/new', views.shows_new),
    path('shows/create', views.create),
    path('shows/<int:id>', views.shows),
    path('shows/<int:id>/edit', views.shows_edit),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>/destroy', views.destroy)
]
