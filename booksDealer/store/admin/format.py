from django.contrib import admin
from ..models import Format


def delete_line(queryset):
    queryset.delete()


class FormatAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')
    search_fields = ['name']
    list_display_links = ['name']

    actions = [delete_line]


admin.site.register(Format, FormatAdmin)
