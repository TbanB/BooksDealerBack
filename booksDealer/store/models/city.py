from django.db import models
from .country import Country


class City(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    country = models.ForeignKey(Country, max_length=150, null=True, blank=True, on_delete=models.SET_NULL)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name