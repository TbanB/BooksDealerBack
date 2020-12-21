from django.contrib import admin
from ..models import Country


def delete_line(queryset):
    queryset.delete()


class CountryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')
    search_fields = ['name']
    list_display_links = ['name']

    actions = [delete_line]


admin.site.register(Country, CountryAdmin)
