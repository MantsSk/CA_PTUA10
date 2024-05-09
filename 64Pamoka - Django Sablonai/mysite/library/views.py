from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book, BookInstance, Author
# Create your views here.


def index(request):
    book_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()
    available_book_instance_count = BookInstance.objects.filter(status='g').count()
    author_count = Author.objects.all().count()

    data = {
        'book_count': book_count,
        'book_instance_count': book_instance_count,
        'available_book_instance_count': available_book_instance_count,
        'author_count': author_count
    }

    return render(request, 'index.html', context=data)
