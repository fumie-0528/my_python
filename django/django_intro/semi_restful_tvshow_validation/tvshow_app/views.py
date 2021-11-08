from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Tvshow

def index(request):
    context = {
    'tvshows': Tvshow.objects.all()
    }
    return render(request, "shows.html", context)

def shows_new(request):
    return render(request,"shows_new.html" )
    
def create(request):
    if request.method == 'POST':
        errors = Tvshow.objects.basic_validator(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            shows=Tvshow.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],description=request.POST['description'])
            return redirect(f'/shows/{show.id}')
    return redirect('/shows/new')

def shows(request,id):

    
    one_show = Tvshow.objects.get(id=id)
    context = {
        'tvshow': one_show
    }
    return render(request, 'shows_detail.html', context)


def shows_edit(request, id):
    one_show = Tvshow.objects.get(id=id)
    context = {
        'tvshow': one_show
    }
    return render(request, 'edit.html', context)


def update(request, id):
    to_update = Tvshow.objects.get(id=id)
    to_update.title = request.POST['title']
    to_update.network = request.POST['network']
    to_update.release_date = request.POST['release_date']
    to_update.description = request.POST['description']
    to_update.save()
    return redirect('/')

def destroy(request, id):
    destroy = Tvshow.objects.get(id=id)
    destroy.delete()
    return redirect('/')
