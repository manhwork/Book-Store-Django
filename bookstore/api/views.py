# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
import json
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'user or password not correct!')
    context = {}
    return render(request, 'login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')