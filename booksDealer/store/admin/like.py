from django.contrib import admin
from ..models import Like


def delete_line(queryset):
    queryset.delete()


class LikeAdmin(admin.ModelAdmin):
    fields = ['value', 'user']
    list_display = ('id', 'value', 'user')
    search_fields = ['user']
    list_display_links = ['user']

    actions = [delete_line]


admin.site.register(Like, LikeAdmin)
