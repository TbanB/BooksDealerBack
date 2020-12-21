from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, default=None)
    birthday = models.DateField(default=now)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
