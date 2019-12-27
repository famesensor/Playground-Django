from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from book_management.models import Category, Book

# Create your views here.
def index(request) :
    context = {
        'cat_num' : len(Category.objects.all()),
        'book_num' : len(Book.objects.all())
    }
    return render(request, 'index.html', context)
    # return HttpResponse("<h1>Hi, Welcome to library</h1>")
