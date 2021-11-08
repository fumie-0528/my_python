from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('show_books', views.show_books),
    path('books/<int:book_id>', views.detail_books),
    path('authors', views.authors),
    path('show_authors', views.show_authors),
    path('authors/<int:author_id>', views.detail_authors),
]