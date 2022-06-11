from importlib.resources import path
from os import name
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('books/',views.books,name='books'),
    path('authors/',views.authors,name='authors'),
    path('contact/',views.contact,name='contact'),
    path('books/<int:id>',views.bookview,name='bookview'),
    
]
