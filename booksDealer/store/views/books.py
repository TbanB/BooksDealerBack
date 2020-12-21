from django.http import HttpResponse
from django.views.generic import ListView
from ..models import Book

class BookListView(ListView):
    model = Book

    def get(self, request):
        res = self.model.objects.all()
        print(res)
        response = HttpResponse()
        # RFC 1123 date format
        response['books'] = res
        return response
