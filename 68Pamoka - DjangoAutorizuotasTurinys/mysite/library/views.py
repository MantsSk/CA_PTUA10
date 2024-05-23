from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from library.models import Book, BookInstance, Author
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    book_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()
    available_book_instance_count = BookInstance.objects.filter(status="g").count()
    author_count = Author.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    data = {
        "book_count": book_count,
        "book_instance_count": book_instance_count,
        "available_book_instance_count": available_book_instance_count,
        "author_count": author_count,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=data)


def authors(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 2)
    page_number = request.GET.get('page')
    paginated_authors = paginator.get_page(page_number)
    context = {"authors": paginated_authors}
    return render(request, "authors.html", context=context)


def search(request):
    search_query = request.GET.get('query')
    search_results = Book.objects.filter(Q(title__icontains=search_query) | Q(summary__icontains=search_query))
    context = {
        'query': search_query,
        'books': search_results
    }
    return render(request, 'search.html', context=context)


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {"author": author}
    return render(request, "author.html", context=context)


class MyBookListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    context_object_name = "book_instance_list"
    template_name = "my_book_list.html"
    # queryset = BookInstance.objects.filter(due_back='2024-05-29')

    def get_queryset(self):
        return BookInstance.objects.filter(reader=self.request.user)

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    # patys galite nustatyti šablonui kintamojo vardą
    context_object_name = "book_list"
    # gauti sąrašą  knygų su pavadinimu
    # queryset = Book.objects.filter(title='Title 1')
    template_name = "book_list.html"
    paginate_by = 2

    # def get_queryset(self):
    #         return Book.objects.filter(title='Title 1')

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['data'] = 'random text'
    #     return context


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = "book_detail.html"
