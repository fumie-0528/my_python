from django.shortcuts import render, redirect
from .models import Book, Author

def books(request):
    context = {
        "books": Book.objects.all(),
        }	
    return render(request, "index.html", context)
    

def show_books(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
    )
    return redirect('/')

def detail_books(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "authors": Author.objects.all()
    }
    return render(request,'book.html', context)

def authors(request):
    context = {
    "authors": Author.objects.all(),
    }	
    return render(request, "authors.html", context)

def show_authors(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    return redirect("/authors")

def detail_authors(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.all()
    }
    return render(request, 'author_view.html', context)
