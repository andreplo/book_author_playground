from django.shortcuts import render
from django.core.cache import cache
from .models import Author
# Create your views here.

def author_list(request):
    authors = cache.get("authors")
    if not authors:
        authors = list(Author.objects.prefetch_related("books").all())
        cache.set("authors", authors, timeout=30)  # cache for 30s
    return render(request, "core/author_list.html", {"authors": authors})