from django.db import models

from core.models import TypeChoices, StatusChoices
from printers.models import Printer


class Check(models.Model):
    """
    Django ORM model to represent 'checks' table.
    """
    check_type = models.CharField(max_length=7, choices=TypeChoices.choices)
    order = models.JSONField()
    status = models.CharField(max_length=8, choices=StatusChoices.choices, default=StatusChoices.NEW)
    pdf_file = models.FileField(null=True, blank=True)

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, related_name='checks')
