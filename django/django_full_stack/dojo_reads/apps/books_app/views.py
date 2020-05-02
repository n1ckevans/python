from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from apps.books_app.models import *
import bcrypt
from datetime import date, datetime

def load_page():
    
   
    Author.objects.create(name="Jane Austen") 
   
   

# # load_page()
# Book.objects.all().delete()
# Author.objects.all().delete()
# Review.objects.all().delete()


def index(request):
    return render(request, "books_app/index.html")

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
    print(new_user.id)
    return redirect("/home")

def home(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect("/")
  
    user = User.objects.get(id=user_id)
    books = Book.objects.all()
    authors = Author.objects.all()


    context = {"user": user, "books": books, "authors" : authors}
    return render(request, "books_app/books.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book_and_review(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    print(request.POST)
    new_review = Review.objects.create(review=request.POST['review'], rating=int(request.POST['rating']), user=user)
    author_exists = Author.objects.filter(name=request.POST['author'])
    book = Book.objects.create(title=request.POST['title'], review=new_review)
    book_id = book.id

    if author_exists:
        author = Author.objects.get(name=request.POST['author'])
    else:
        author = Author.objects.create(name=request.POST['author'])

   
    # rating=int(request.POST['rating'])

    return redirect(f"/book/{book_id}")



def book(request, book_id):
    context = {
        "book": Book.objects.get(id=int(book_id)),
        "authors": Author.objects.all().exclude(books__in=Book.objects.filter(id=int(book_id)))
    }
    return render(request, "books_app/book_view.html", context)


