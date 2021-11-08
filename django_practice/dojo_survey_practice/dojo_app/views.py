from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        context={
            'your_name': request.POST['your_name'],
            'dojo_location': request.POST['dojo_location'],
            'favorite_language':request.POST['favorite_language'] 
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')


