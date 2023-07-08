from django.db import models
# from django.db.models.functions import Concat, F
# from django.db.models import CharField, Value

import PIL

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254)
    phone_number = models.PositiveIntegerField()

class Author(models.Model): # *should the author have their own class or can they be directly included in the book class without external referencing?
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name

class Book(models.Model):
    GENRES = [
        ("CRIME", "Crime"),
        ("FANTASY", "Fantasy"),
        ("MYSTERY", "Mystery"),
        ("ROMANCE", "Romance"),
        ("SCI-FI", "Sci-Fi"),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    genre = models.CharField(max_length=7, choices=GENRES)
    thumbnail = models.ImageField(upload_to="media")
    blurb = models.TextField()
    # availability = # *an input field, so it should probably be in its own class and be externally referenced.

    def __str__(self):
        return self.title

'''
class Availability(models.Model):
    borrow_date = models.DateField() # *date input by Person
    return_date = models.DateField() # *date input by Person
'''