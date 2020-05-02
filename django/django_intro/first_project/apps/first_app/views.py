from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
    	"name": "Nick",
    	"favorite_color": "Dodger Blue",
    	"pets": ["Ghost", "Nala"]
    }
    return render(request, "first_app/index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a blog")

def create(request):
    return redirect("/")

def show(request, my_val):
    return HttpResponse(f"placeholder to display blog number: {my_val}")

def edit(request, my_val):
    return HttpResponse(f"placeholder to edit blog number: {my_val}")

def destroy(request, my_val):
    return redirect("/")
