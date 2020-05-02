from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __repr__(self):
        return f"<Book object: id: {self.id}, title: {self.title}>"

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(default="Author notes")

    def __repr__(self):
        return f"<Author object: id: {self.id}, first name: {self.first_name}, last name: {self.last_name}>"