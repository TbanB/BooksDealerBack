from django.contrib import admin
from ..models import Rate


def delete_line(queryset):
    queryset.delete()


class RateAdmin(admin.ModelAdmin):
    fields = ['book', 'user', 'value']
    list_display = ('id', 'book', 'user', 'value')
    search_fields = ['book', 'user', 'value']
    list_display_links = ['id']

    actions = [delete_line]


admin.site.register(Rate, RateAdmin)
