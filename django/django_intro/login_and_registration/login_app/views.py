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
