# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request,"home/index.html",context)