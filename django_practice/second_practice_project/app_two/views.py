from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")

def create(request):
    return redirect('/blog') 

def blog(request):
    return HttpResponse('what does this do')

def show(request, number):
    return HttpResponse(f'placeholder to display blog number{number}')

def edit(request, number):
    return HttpResponse(f'placeholder to deit blog number{number}')

def destroy(request):
    return redirect('/')
