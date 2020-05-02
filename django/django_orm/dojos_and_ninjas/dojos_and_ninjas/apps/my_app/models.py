from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255, default="A description of the dojo")
    #ninjas = a list of ninjas associated with a given dojo

    def __repr__(self):
        return f"<Dojo object: (id:{self.id}), name:{self.name}, city:{self.city}, state: {self.state}>"

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return f"<Ninja object: (id:{self.id}), dojo: {self.dojo}, first name:{self.first_name}, last name: {self.last_name}>"