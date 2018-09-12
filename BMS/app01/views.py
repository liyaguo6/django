from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django.urls import reverse


# Create your views here.

# 出版社
def publisher_list(request):
    data = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': data})


def add_publisher(request):
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        publisher_address = request.POST.get('publisher_address')
        models.Publisher.objects.create(name=publisher_name, address=publisher_address)
        return redirect(reverse('publisher_list'))
    return render(request, 'add_publisher.html')


def delete_publisher(request, id):
    models.Publisher.objects.get(id=id).delete()
    return redirect(reverse('publisher_list'))


def edit_publisher(request, edit_id):
    if request.method == 'POST':
        publisher_id = request.POST.get('publisher_id')
        edit_obj = models.Publisher.objects.get(id=publisher_id)
        edit_obj.name = request.POST.get('publisher_name')
        edit_obj.address = request.POST.get('publisher_address')
        edit_obj.save()
        return redirect(reverse('publisher_list'))
    edit_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'edit_publisher.html', {'publisher_obj': edit_obj})


# 书
def books_list(request):
    data = models.Book.objects.all()
    return render(request, 'books_list.html', {'books_list': data})


def add_books(request):
    if request.method == 'POST':
        title = request.POST.get('books_name')
        date = request.POST.get('books_pubdate')
        publisher = request.POST.get('publisher_id')  # 一对多记录添加
        models.Book.objects.create(title=title, date=date, publisher_id=publisher)
        return redirect(reverse('books_list'))
    data = models.Publisher.objects.all()
    return render(request, 'add_books.html', {'publisher_list': data})


def delete_books(request, id):
    models.Book.objects.get(id=id).delete()
    return redirect(reverse('books_list'))


def edit_books(request, edit_id):
    if request.method == 'POST':
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.title = request.POST.get('edit_books.bname')
        edit_obj.date = request.POST.get('edit_books.pubdate')
        edit_obj.publisher_id = request.POST.get('publisher_id')
        edit_obj.save()
        return redirect(reverse('books_list'))
    edit_obj = models.Book.objects.get(id=edit_id)
    publisher_list = models.Publisher.objects.all()
    return render(request, 'edit_books.html', {'edit_books': edit_obj, 'publisher_list': publisher_list})


# 作者
def author_list(request):
    data = models.Author.objects.all()
    return render(request, 'author_list.html', {'author_list': data})


def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        # author_obj = models.Author.objects.get(name=author_name)
        authors = models.Author.objects.all().values('name')
        for author in authors:
            if author_name == author.get("name"):
                author_obj = models.Author.objects.get(name=author_name)
                break
        else:
            author_obj = models.Author.objects.create(name=author_name)
        books_id_list = request.POST.getlist('books_id')
        for books_id in books_id_list:
            book_obj = models.Book.objects.get(id=books_id)
            author_obj.books.add(book_obj)
        return redirect(reverse('author_list'))
    data = models.Book.objects.all()
    return render(request, 'add_author.html', {'books_list': data})


def delete_author(request, delete_id):
    author_obj = models.Author.objects.get(id=delete_id)
    author_obj.books.clear()
    author_obj.delete()
    return redirect(reverse('author_list'))


def edit_author(request, edit_id):
    edit_obj = models.Author.objects.get(id=edit_id)
    if request.method == 'POST':
        author_name=request.POST.get('author_name')
        books_id=request.POST.getlist('books_id')
        edit_obj.name =author_name
        edit_obj.books.set(books_id)
        edit_obj.save()
        return redirect(reverse('author_list'))
    edit_obj=models.Author.objects.get(id=edit_id)
    books_list = models.Book.objects.all()
    return render(request,'edit_author.html',{'author_obj':edit_obj,'book_list':books_list})

def login(request):
    pass
