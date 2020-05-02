from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from apps.login_app.models import *
import bcrypt

# User.objects.all().delete()

def index(request):
    return render(request, "login_app/index.html")

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


def home(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")
    
    user = User.objects.get(id=user_id)
    

    context = {"user": user}
    return render(request, "login_app/welcome.html", context)

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