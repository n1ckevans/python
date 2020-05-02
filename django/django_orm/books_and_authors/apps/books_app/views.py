from django.shortcuts import render, HttpResponse, redirect
from .models import *

def load_page():
    Book.objects.all().delete()
    Author.objects.all().delete()
    Book.objects.create(title="C#", desc="A book about C#")
    Book.objects.create(title="Java", desc="A book about Java") 
    Book.objects.create(title="Python", desc="A book about Python") 
    Book.objects.create(title="PHP", desc="A book about PHP")
    Book.objects.create(title="Ruby", desc="A book about Ruby") 
    Author.objects.create(first_name="Jane", last_name="Austen") 
    Author.objects.create(first_name="Emily", last_name="Dickinson")
    Author.objects.create(first_name="Fyodor", last_name="Dostoevksy")
    Author.objects.create(first_name="William", last_name="Shakespeare") 
    Author.objects.create(first_name="Lau", last_name="Tzu")    
    c = Book.objects.get(title="C#") 
    bill = Author.objects.get(first_name="William")
    jane = Author.objects.get(first_name="Jane") 
    java = Book.objects.get(title="Java")
    jane.books.add(c)
    jane.books.add(java) 
    emily = Author.objects.get(first_name="Emily")
    fyodor = Author.objects.get(first_name="Fyodor") 
    lau = Author.objects.get(first_name="Lau") 
    python = Book.objects.get(title="Python") 
    php = Book.objects.get(title="PHP")
    ruby = Book.objects.get(title="Ruby") 
    emily.books.add(c, java, python)
    fyodor.books.add(c, java, python, php) 
    bill.books.add(c, java, python, php, ruby)
    python.authors.all() 
    python.authors.remove(emily) 
    lau.books.add(java)




load_page()

def index(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }
    

    return render(request, "books_app/index.html", context)

def book(request, book_id):
    if request.method == "POST":
        Book.objects.get(id=int(book_id)).authors.add(Author.objects.get(id=request.POST["author"]))
        return redirect(f"/books/{book_id}")

    context = {
        "book": Book.objects.get(id=int(book_id)),
         "authors": Author.objects.all().exclude(books__in=Book.objects.filter(id=int(book_id)))
    }

    return render(request, "books_app/books.html", context)

def add_book(request):
    title = request.POST['title']
    desc = request.POST['description']
    Book.objects.create(title=title, desc=desc)
    return redirect('/')

def all_authors(request):

    context = {
        "authors": Author.objects.all()
    }
    
    return render(request, "books_app/authors.html", context)

def add_author(request):
    first = request.POST['first_name']
    last = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=first, last_name=last, notes=notes)
    return redirect('/authors')

def author(request, auth_id):
    if request.method == "POST":
        Author.objects.get(id=auth_id).books.add(Book.objects.get(id=request.POST["book"]))
        return redirect(f"/authors/{auth_id}")

    context = {
        "author": Author.objects.get(id=int(auth_id)),
         "books": Book.objects.all().exclude(authors__in=Author.objects.filter(id=int(auth_id)))
    }

    return render(request, "books_app/author.html", context)

