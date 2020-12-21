from django.contrib import admin
from ..models import Distributor


def delete_line(queryset):
    queryset.delete()


class DistributorAdmin(admin.ModelAdmin):
    fields = ['name', 'country', 'city', 'postal_code', 'address']
    list_display = ('id', 'name', 'country', 'city', 'postal_code', 'address')
    list_display_links = ['name']
    search_fields = ['name', 'country', 'city', 'postal_code', 'address']

    actions = [delete_line]


admin.site.register(Distributor, DistributorAdmin)
