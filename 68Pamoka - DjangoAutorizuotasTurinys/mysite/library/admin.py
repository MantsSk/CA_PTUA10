from django.contrib import admin
from library.models import Genre, Author, BookInstance, Book

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    can_delete = False
    readonly_fields = ('due_back', )


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'summary', 'display_genres')
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_editable = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'reader')
    list_filter = ('status', 'due_back')
    search_fields = ('due_back', 'book__title')
    fieldsets = (
        ('General', {
            'fields': ('book',)
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'reader')
        })
    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_books')


# Register your models here.
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Book, BookAdmin)