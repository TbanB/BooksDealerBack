from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Sum

from . import Book


class Rate(models.Model):
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, max_length=150, null=True, on_delete=models.SET_NULL)
    value = models.IntegerField(default=0,
                                validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.book.name} '

    def get_total_rate_value(self):
        return Rate.objects.filter(id=self.book.id).aggregate(Sum('value')) / Rate.objects.filter(
            id=self.book.id).count()
