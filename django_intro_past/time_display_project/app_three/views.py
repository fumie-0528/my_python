from django.shortcuts import render,HttpResponse
from time import gmtime, strftime 

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'html/index.html', context)