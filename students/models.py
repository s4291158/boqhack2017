from django.db import models
from django.utils import timezone
from persons.models import Person


class Student(Person):
    referrer = models.ForeignKey(
        'self',
        null=True,
        blank=True
    )
    student_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    degree = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    faculty = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    graduation_year = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    is_paying_member = models.BooleanField(
        default=True
    )
    day_of_signup = models.DateTimeField(
        default=timezone.now,
        blank=True
    )
    role = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'student {}'.format(self.id)
