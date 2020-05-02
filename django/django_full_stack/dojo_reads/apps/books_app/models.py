from django.db import models
from django.core.validators import validate_email
from django.contrib import messages
from django.contrib.messages import get_messages
import re
from datetime import date, datetime, timedelta
import timeago 



class UserManager(models.Manager):
    def is_reg_valid(self, request):

        if len(request.POST['first_name']) < 2:
            messages.error(request, "First Name should be at least 2 characters")

        if len(request.POST['last_name']) < 2:
            messages.error(request, "Last Name should be at least 2 characters")

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.error(request, "Invalid email")

        if len(request.POST['password']) < 8:
            messages.error(request, "Password should be at least 8 characters")

        if request.POST['password'] != request.POST['confirm_password']:
            messages.error(request, "Passwords do not match")

        birthday = datetime.strptime(request.POST['birthday'], "%Y-%m-%d")
        today = date.today()
        now = datetime.now()
        age = (today.year - birthday.year -
        ((today.month, today.day) <
        (birthday.month, birthday.day)))

        if birthday > datetime.today():
           messages.error(request, "Birthday can not be a future date")
        
        if age < 13:
            messages.error(request, "Must be at least 13 to register")

        storage = messages.get_messages(request)
        storage.used = False
        return len(storage) == 0

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateField()
    objects = UserManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Book(models.Model):
    title = models.CharField(max_length=255)
    review = models.ForeignKey(Review, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Book object: id: {self.id}, title: {self.title}>"



class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Author object: id: {self.id}, first name: {self.first_name}, last name: {self.last_name}>"