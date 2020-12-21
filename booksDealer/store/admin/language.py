from django.contrib import admin
from ..models import Language


def delete_line(queryset):
    queryset.delete()


class LanguageAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')
    search_fields = ['name']
    list_display_links = ['name']

    actions = [delete_line]


admin.site.register(Language, LanguageAdmin)
