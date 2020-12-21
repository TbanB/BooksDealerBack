from django.contrib import admin
from ..models import Author


def delete_line(queryset):
    queryset.delete()


class AuthorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'birthday']
    list_display = ('id', 'first_name', 'last_name', 'birthday')
    search_fields = ['first_name', 'last_name']
    list_display_links = ['first_name']

    actions = [delete_line]


admin.site.register(Author, AuthorAdmin)
