from django.shortcuts import render
from django.core.cache import cache
from .models import Author, Book
# Create your views here.

def author_list(request):
    authors = cache.get("authors")
    print(f"Authors exist: {cache.has_key('authors')}")
    if not authors:
        print("--------Redis Miss")
        authors = list(Author.objects.prefetch_related("books").all())
        cache.set("authors", authors, timeout=300)  # cache for 300s = 5min
    return render(request, "core/author_list.html", {"authors": authors})

def books_list(request):
    books = cache.get("books")
    print(f"Books -redis- : [{books}]")
    if not books:
        books = list(Book.objects.all())
        cache.set("books", books, timeout=300) #cache for 300s = 5min too
    return render(request, "core/books_list.html", {"books": books})