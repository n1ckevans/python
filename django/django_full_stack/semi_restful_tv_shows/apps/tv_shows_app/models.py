from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if datetime.strptime(postData['release_date'], "%Y-%m-%d") > datetime.today():
           errors["release_date"] = "Release date should be in the past"
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors["description"] = "Description should either be blank, or greater than 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Book object: id: {self.id}, title: {self.title}>"

