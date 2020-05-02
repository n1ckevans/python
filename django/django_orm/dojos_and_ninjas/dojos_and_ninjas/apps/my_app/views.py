from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Is this thing on?")

