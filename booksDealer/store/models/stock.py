
from django.db import models

from . import Book


class Stock(models.Model):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL)
    stock = models.IntegerField(blank=False, null=False, default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.book.name} - Units: {self.stock}'
