from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from library.models import Book, BookInstance, Author
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.shortcuts import redirect

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

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    try:
                        validate_password(password)
                    except ValueError as e:
                        for error in e.args[0]:
                            messages.error(request, error)
                        return redirect('register')

                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')

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

def validate_password(password):
    errors = []

    # Check for minimum length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # Check for presence of digits
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")

    # Check for presence of uppercase letters
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Check for presence of lowercase letters
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    if errors:
        raise ValueError(errors)