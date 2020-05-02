from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("Yo, What's Up G?")

def random(request):
    request.session['random_word'] = get_random_string(length=14)
    if not request.session.get('counter'):
        request.session['counter'] = 0
    if request.method == "POST":
        request.session['counter'] += 1
    elif request.method == "GET":
        request.session['counter'] = 0
        request.session['random_word'] = ""
    return render(request, "random_word_app/index.html")
