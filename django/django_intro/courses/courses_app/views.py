from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def process(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            course = Course.objects.create(name=request.POST['name'],description=request.POST['description'])
            return redirect('/')
    return redirect('/')


def remove(request, id):
    if request.method == "GET":
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request,"remove.html" , context)

    if request.method == "POST":
        remove = Course.objects.get(id=id)
        remove.delete()
        return redirect('/')
