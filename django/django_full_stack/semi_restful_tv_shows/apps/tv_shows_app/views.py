from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def shows(request):

    context = {
    "all_shows": Show.objects.all(),
    }
    
    return render(request, "tv_shows_app/index.html", context)

def add_show(request):
    return render(request, "tv_shows_app/new.html")


def create_show(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        print(description)
        print(release_date)
        newShow = Show.objects.create(title=title, network=network, release_date=release_date, description=description)

        return redirect(f"/shows/{newShow.id}")

def new_show(request, newShow_id):
    context = {
        "new_show": Show.objects.get(id=int(newShow_id)),
    }

    return render(request, "tv_shows_app/show.html", context)

def edit_show(request, newShow_id):
    context = {
        "new_show": Show.objects.get(id=int(newShow_id))
    }
    return render(request, "tv_shows_app/edit.html", context)

def update_show(request, newShow_id):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect(f"/shows/{newShow_id}/edit_show")

    else:
        oldShow = Show.objects.get(id=newShow_id)
        
        oldShow.title = request.POST['title']
        oldShow.network = request.POST['network']
        oldShow.release_date = request.POST['release_date']
        oldShow.description = request.POST['description']
        oldShow.save()
    
        return redirect(f"/shows/{newShow_id}")

def delete(request, newShow_id):
    show = Show.objects.get(id=newShow_id)
    show.delete()
    return redirect('/')