from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def random_word(request):  
    context = {
        'word':get_random_string(length=14)
    }
    request.session['count'] = 0
    count = request.session['count']
    if 'count' not in request.session:
        request.session['count'] += 1
        return count
    return render(request, 'index.html', context)

def reset(request):
    request.session.flush()
    return redirect('/random_word')
