from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def process(request):
    request.session['your_name']=request.POST['your_name']
    request.session['location']=request.POST['location']
    request.session['favorite_language']=request.POST['favorite_language']
    request.session['comment']=request.POST['comment']
    return redirect('/result')



def result(request):

    context = {
    "your_name": request.session["your_name"],
    "location": request.session["location"],
    "favorite_language": request.session["favorite_language"],
    "comment": request.session["comment"]
    }
    return render(request, 'result_index.html', context)
    



