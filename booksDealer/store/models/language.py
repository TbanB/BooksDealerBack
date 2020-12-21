from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name
