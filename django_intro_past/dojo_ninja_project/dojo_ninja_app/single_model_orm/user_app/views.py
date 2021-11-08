from django.shortcuts import render, redirect 
from .models import User

def index(request):
    context = {
    'users': User.objects.all()
    }
    return render(request, 'index.html', context)


def process(request):
    User.objects.create(
        name=request.POST['name'],
        email_address=request.POST['email'],
        age=request.POST['age']
    )
    return redirect('/')