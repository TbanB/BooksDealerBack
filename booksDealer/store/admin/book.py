from django.contrib import admin
from ..models import Book


def delete_line(queryset):
    queryset.delete()


class BookAdmin(admin.ModelAdmin):
    fields = ['ref', 'name', 'author', 'publisher', 'release_date', 'like', 'url_image', 'format', 'isbn',
              'pages', 'language', 'category', 'price']
    list_display = ('id', 'ref', 'name', 'author', 'publisher', 'release_date', 'like', 'url_image', 'format', 'isbn',
                    'pages', 'language', 'category', 'price')
    search_fields = ['ref', 'name']
    list_display_links = ['ref']

    actions = [delete_line]


admin.site.register(Book, BookAdmin)
