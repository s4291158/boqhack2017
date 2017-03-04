from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
