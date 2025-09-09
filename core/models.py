from django.db import models
from django.contrib import admin

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
admin.site.register(Author)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_at = models.DateField()

    def __str__(self):
        return self.title
admin.site.register(Book)


