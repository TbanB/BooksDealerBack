import uuid

from django.utils.timezone import now
from django.db import models

from .language import Language
from .distributor import Distributor
from .category import Category
from .format import Format
from .author import Author

from .like import Like


class Book(models.Model):
    ref = models.CharField(max_length=36, blank=False, null=False, default=uuid.uuid4)
    name = models.CharField(max_length=150, blank=False, null=False)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Distributor, null=True, blank=True, on_delete=models.SET_NULL)
    release_date = models.DateField(blank=False, null=False, editable=True,
                                    default=now)
    like = models.ForeignKey(Like, null=True, blank=True, on_delete=models.SET_NULL)
    url_image = models.CharField(max_length=150, blank=False, null=False)
    format = models.ForeignKey(Format, null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=150, blank=False, null=False)
    pages = models.IntegerField(blank=False, null=False)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField(blank=False, null=False, default=0.0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name
