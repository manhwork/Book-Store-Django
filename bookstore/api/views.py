# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"home/index.html",{
        "title" : "Home",
    })

def books(request):
    return render(request,"books/index.html",{
        "title" : "Books",
    })

def author_about(request):
    return render(request, "author_about/index.html",{
        "title" : "Author About",
    })