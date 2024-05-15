from django.shortcuts import get_object_or_404, render
from library.models import Book, BookInstance, Author
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def index(request):
    book_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()
    available_book_instance_count = BookInstance.objects.filter(status="g").count()
    author_count = Author.objects.all().count()

    data = {
        "book_count": book_count,
        "book_instance_count": book_instance_count,
        "available_book_instance_count": available_book_instance_count,
        "author_count": author_count,
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


class BookListView(generic.ListView):
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


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book_detail.html"
