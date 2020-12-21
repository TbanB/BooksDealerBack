from django.contrib import admin
from ..models import City


def delete_line(queryset):
    queryset.delete()


class CityAdmin(admin.ModelAdmin):
    fields = ['name', 'country']
    list_display = ('id', 'name', 'country')
    list_display_links = ['name']
    search_fields = ['name', 'country']

    actions = [delete_line]


admin.site.register(City, CityAdmin)
