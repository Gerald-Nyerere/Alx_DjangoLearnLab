from django.db import models

# Create your models here.

# Author model stores details about book authors
class Author(models.Model):
    name = models.CharField(max_length=200)

# Book model represents individual books
# Each book is linked to one Author via a ForeignKey relationship
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

