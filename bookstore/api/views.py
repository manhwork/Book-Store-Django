# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    
    return render(request,"home/index.html",{
        "title" : "Home",
    })

def books(request):
    l=Book.objects.all()
    print(l)
    return render(request,"books/index.html",context={
        "title" : "Books",
        "books":l
    })

def author_about(request):
    return render(request, "author_about/index.html",{
        "title" : "Author About",
    })

def contact(request):
    return render(request, "contact/index.html",{
        "title" : "Contact",
    })

def blog(request):
    return render(request, "blog/index.html",{
        "title" : "Blog",
    })