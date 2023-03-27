from django.db import models

from core.models import TypeChoices, StatusChoices


class Printer(models.Model):
    """
    Django ORM model to represent 'printers' table.
    """
    name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=50)
    check_type = models.CharField(max_length=7, choices=TypeChoices.choices)
    point_id = models.IntegerField()

    @staticmethod
    def print_check(check):
        """
        Change check status from 'rendered' to 'printed'.
        """
        check.status = StatusChoices.PRINTED
        check.save()

    def __str__(self):
        return self.name
