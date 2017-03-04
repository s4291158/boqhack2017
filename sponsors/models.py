from django.db import models
from persons.models import Person


class Contact(Person):
    pass


class Sponsors(models.Model):
    point_of_contact = models.OneToOneField(
        Contact,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    potential_score = models.IntegerField(
        choices=(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ),
        null=True,
        blank=True
    )
    max_estimated_value = models.IntegerField(
        null=True,
        blank=True
    )
    min_estimated_value = models.IntegerField(
        null=True,
        blank=True
    )
