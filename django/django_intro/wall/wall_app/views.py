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
            'user': user
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

def message(request):
    message = Message.objects.all()
    user = User.objects.all()
    context = {
        'messages': message,
        'user:' : user
    }
    return render(request, "wall.html", context)

def post_message(request):
    Message.objects.create(
        message_text=request.POST['message'], 
        user=User.objects.get(id=request.session['user_id']))
    return redirect('/message')

def post_comment(request, id):  
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=id)
    Comment.objects.create(comment_text=request.POST['comment'], user=user, message=message)
    return redirect('/message')

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete() 
    return redirect('/message')