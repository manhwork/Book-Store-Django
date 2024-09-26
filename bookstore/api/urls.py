from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/",views.books,name="books"),
    # path("about_author/",views.books,name="about_author"),
    # path("contact/",views.books,name="contact"),
]