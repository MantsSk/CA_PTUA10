from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField('Name', max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Zanras'
        verbose_name_plural = 'Zanrai'




class Author(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def display_books(self):
        return ', '.join(book.title for book in self.books.all())


class Book(models.Model):
    title = models.CharField('Title', max_length=200)
    summary = models.TextField('Summary', max_length=1000)
    isbn = models.CharField('ISBN', max_length=13)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title}'
    
    def display_genres(self):
        return ', '.join(genre.name for genre in self.genre.all())


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField('Due back', null=True, blank=True)

    STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota')
    )
    status = models.CharField('Status', max_length=1, default='a', choices=STATUS)

    def __str__(self):
        return f'{self.due_back}'
