from django.contrib import admin
from ..models import Category


def delete_line(queryset):
    queryset.delete()


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')
    search_fields = ['name']
    list_display_links = ['name']

    actions = [delete_line]


admin.site.register(Category, CategoryAdmin)
