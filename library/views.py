from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
# from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Book
from django.db import IntegrityError




def start(request:HttpRequest):
    return redirect('/books/')



def home(request:HttpRequest):
    books = Book.objects.all()

    query = request.GET.get('query')
    if query:
        books = books.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        query = ''

    min_price = request.GET.get('min_price')
    if min_price:
        books = books.filter(price__gte=min_price)
    max_price = request.GET.get('max_price')
    if max_price:
        books = books.filter(price__lte=max_price)

    publication_at = request.GET.get('publication_at')
    if publication_at:
        books = books.filter(publication_at=publication_at)


    context = {
        'books':books,'query':query,'min_price':min_price,
        'max_price':max_price,'publication_at':publication_at,
    }
    return render(request,'library_home.html',context=context)



def add_book(request:HttpRequest):
    message = ''
    if request.method == "POST":
        title  = request.POST.get('title')
        author = request.POST.get('author')
        price  = float(request.POST.get('price'))

        try:
            Book.objects.create(title=title,author=author,price=price)
            return redirect('/books/')
        except IntegrityError as e: 
            message = 'This book is already available with this author!'

    return render(request,'add_book.html',{'message':message})



def edit_book(request:HttpRequest, id):
    book = get_object_or_404(Book,id=id)

    message = ''
    if request.method == "POST":
        title  = request.POST.get('title')
        author = request.POST.get('author')
        price  = float(request.POST.get('price'))

        book.title  = title
        book.author = author
        book.price  = price
        try:
            book.save()
            return redirect('/books/')
        except IntegrityError as e: 
            message = 'This book is already available with this author!'

    return render(request,'edit_book.html',{'book':book,'message':message})



def delete_book(request:HttpRequest, id):
    book = get_object_or_404(Book,id=id)
    book.delete()

    return redirect("/books/")



# def search_books(request):
#     query = request.GET.get('query')
#     books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)

#     context = {'books':books,}
#     return render(request,'library_home.html',context=context)



# paginator = Paginator(books,6)
# get_page=request.GET.get('page')
# try:
#     books = paginator.page(get_page)
# except PageNotAnInteger:
#     books = paginator.page(1)
# except EmptyPage:
#     books = paginator.page(paginator.num_pages)
