
from multiprocessing import context
from os import name
from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Author, Book, BookInstance
# Create your views here.


def index(request):
    num_visit=request.session.get('num_visit',0)
    request.session['num_visit']=num_visit + 1
    book=Book.objects.all()
    book_avail=BookInstance.objects.all().count()
    author=Author.objects.all()
    context={
        'book':book,
        'book_avail':book_avail,
        'author':author,
        'num_visit':num_visit
    }
    return render(request,'catalog/index.html',context=context)

def authors(request):
    return render(request,'catalog/authors.html')

def books(request):
    num_visit=request.session.get('num_visit',0)
    request.session['num_visit']=num_visit + 1
    book=Book.objects.all()
    book_avail=BookInstance.objects.all().count()
    author=Author.objects.all()
    context={
        'book':book,
        'book_avail':book_avail,
        'author':author,
        'num_visit':num_visit
    }
    return render(request,'catalog/books.html',context=context)


def contact(request):
    return render(request,'catalog/contact.html')

def bookview(request,id):
    book=Book.objects.filter(id=id)
    author=Author.objects.filter(id=id)
    context={
        'book':book,
        'author':author
    }
    return render(request,'catalog/bookview.html',context=context)
    
    
    
    
    
    
    
        