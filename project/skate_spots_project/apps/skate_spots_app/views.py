from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.messages import get_messages
from apps.skate_spots_app.models import *
from django.contrib.sites.models import Site
import bcrypt
from datetime import date, datetime


def index(request):
    return render(request, "skate_spots_app/index.html")

def login(request):
    valid_user = User.objects.filter(email=request.POST['email'])
    if valid_user:
        current_user = valid_user[0]

        pw_match = bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode())

        if pw_match:
            request.session['user_id'] = current_user.id
        else:
            messages.error(request, "Invalid credentials")
            return redirect("/")
    else:
        messages.error(request, "Invalid credentials")
        messages.error(request, "Please try again")
        return redirect("/")
    return redirect ("/home")

def register(request):
    taken_user = User.objects.filter(email=request.POST['email'])
    if taken_user:
        messages.error(request, "Invalid credentials")
        return redirect("/")

    if not User.objects.is_reg_valid(request):
        return redirect("/")

    hashed = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())


    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed, birthday=request.POST['birthday'])
    request.session['user_id'] = new_user.id
    return redirect("/home")

def logout(request):
    request.session.clear()
    return redirect('/')

def home(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")

    user = User.objects.get(id=user_id)
    
    all_users = User.objects.all()
    markers = Marker.objects.all()
    print(markers)
   

    context = {"user": user, "markers": markers}
    return render(request, "skate_spots_app/home.html", context)

def wall(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")

  
    user = User.objects.get(id=user_id)
    all_messages = Message.objects.all()
    all_comments = Comment.objects.all()

    context = {"user": user, "messages" : all_messages, "comments" : all_comments}
    return render(request, "skate_spots_app/messages.html", context)


def add_message(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    new_message = Message.objects.create(user = user, message = request.POST['message'], subject=request.POST['subject'])
    request.session['message_id'] = new_message.id
    return redirect("/wall")


def delete(request, message_id):
   message = Message.objects.get(id=message_id)
   message.delete()
   return redirect('/wall')


def add_comment(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    
    message_id = request.POST['comment_id']
    message = Message.objects.get(id=message_id)
   
    new_comment = Comment.objects.create(user = user, message = message, comment = request.POST['comment'])
    return redirect(f"/message/{message_id}")

def message(request, message_id):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")

    message = Message.objects.get(id=message_id)
    user = User.objects.get(id=user_id)
    all_comments = Comment.objects.all()

    context = {"user": user, "message" : message, "comments" : all_comments}
    return render(request, "skate_spots_app/message.html", context)

def profile(request, user_id):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")

    user = User.objects.get(id=user_id)
  

    context = {"user": user,}
    return render(request, "skate_spots_app/user.html", context)

def update(request, user_id):
    taken_user = User.objects.filter(email=request.POST['email'])
    if taken_user:
        messages.error(request, "Invalid credentials")
        return redirect("/")

    if not User.objects.is_reg_valid(request):
        return redirect("/")

    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")

    user = User.objects.get(id=user_id)

    hashed = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())


    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.password = hashed
    birthday = request.POST['birthday']
    photo = request.POST['photo']
    user.save()
    
    return redirect("/home")