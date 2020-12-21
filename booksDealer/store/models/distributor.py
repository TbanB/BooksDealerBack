from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .country import Country
from .city import City


class Distributor(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    country = models.ForeignKey(Country, max_length=150, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, max_length=150, null=True, blank=True, on_delete=models.SET_NULL)
    postal_code = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(000000)], default=000000)
    address = models.CharField(max_length=150, blank=False, null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name
