from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/",views.books, name="books"),
    path("author_about/",views.author_about, name="author_about"),
    # path("contact/",views.books,name="contact"),
]