from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request, error)
            return redirect('/') 
        #if no errors on POST data, run this code. 
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id

        return redirect('/welcome')
    
def welcome(request):
    user = User.objects.get(id=request.session['user_id'])
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            # "book": Book.objects.all(),
            "user": user,
            "user_book": Book.objects.filter(user=user),
            "favorited_book": Book.objects.filter(favorited_by=user),
            "other_books": Book.objects.all().exclude(user=user).exclude(favorited_by=user)
        }
    return render(request, 'welcome.html', context)

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/welcome')

def logout(request):
    request.session.clear()
    return redirect("/")

def add_book(request):
    Book.objects.create(
    name=request.POST['name'], 
    desc=request.POST['desc'],
    user=User.objects.get(id=request.session['user_id']))
    return redirect("/welcome")

def book_detail(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.all()
    context = {
        "book": book,
        "favorited_user": Book.objects.filter(favorited_by=user)
    }
    return render(request,'book.html', context)


def book_edit(request, id):
    book = Book.objects.get(id=id)
    context = {
        "to_update": book
    }
    return render(request, "edit.html", context)

def book_update(request, id):
    to_update = Book.objects.get(id=id)
    to_update.name = request.POST["update_name"]
    to_update.desc= request.POST["update_desc"]
    to_update.save()
    return redirect(f"/book_detail/{id}")

def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete() 
    return redirect("/welcome")

def add_to_favorite(request, id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=id)
    book.favorited_by.add(user)
    return redirect(f'/book_detail/{id}')

def un_favorite(request, id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=id)
    user.user_book.remove(book)

    return redirect(f'/book_detail/{id}') 