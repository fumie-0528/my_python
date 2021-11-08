from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        return redirect('/trips')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/trips')

def logout(request):
    request.session.clear()
    return redirect('/')


def trips(request):
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id = request.session['user_id'])
    context = {
		"user": user,
        "user_trips": Trip.objects.filter(planner=user),
        "joined_trips": Trip.objects.filter(joined=user),
		"other_trips": Trip.objects.all().exclude(planner=user).exclude(joined=user)
	}
    return render(request,"dashboard.html",context)

def new(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request,"new.html",context)

def create(request):
    if request.method == "POST":
        errors = Trip.objects.validate(request.POST)
        if errors:
            # for e in errors.items():
            #     messages.error(request, e)
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/trips/new")
        Trip.objects.create(
            destination =request.POST['destination'],
            plan=request.POST['plan'],
            date_start = request.POST['date_start'],
		    date_end = request.POST['date_end'],
            planner=User.objects.get(id=request.session['user_id'])
        )
    return redirect("/trips")

def detail(request, id):
    trip = Trip.objects.get(id=id)
    user = User.objects.get(id = request.session['user_id'])
    context = {
        "trip": trip,
		"people_trips": Trip.objects.all().exclude(planner=user).exclude(joined=user)
    }
    return render(request,'trip_detail.html', context)

def edit(request, id):
    trip = Trip.objects.get(id=id)
    user = User.objects.get(id = request.session['user_id'])
    context = {
        "to_update": trip,
        "user": user
    }
    return render(request, "edit.html", context)

def update(request, id):
    to_update = Trip.objects.get(id=id)
    to_update.destination = request.POST["update_destination"]
    to_update.plan = request.POST["update_plan"]
    to_update.date_start= request.POST["update_date_start"]
    to_update.date_end= request.POST["update_date_end"]
    to_update.save()
    return redirect(f"/trips/detail/{id}")

def delete(request,id):
    trip = Trip.objects.get(id=id)
    trip.delete() 
    return redirect("/trips")

def join(request,id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    user.joined_trips.add(trip)
    return redirect("/trips")

def cancel(request,id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    user.joined_trips.remove(trip)
    return redirect("/trips")