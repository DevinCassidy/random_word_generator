from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    context={
        "word": get_random_string(length=14)
    }
    if "guesses" in request.session: 
        request.session['guesses'] += 1
    return render(request,"word_app/index.html", context)

def start(request):
    request.session['guesses'] = 0
    return redirect('/')
