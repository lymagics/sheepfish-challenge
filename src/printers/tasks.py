from celery import shared_task

from .models import Printer
from core.models import StatusChoices


@shared_task
def print_checks():
    """
    Print all checks with status 'rendered'.
    """
    for printer in Printer.objects.all():
        for check in printer.checks.filter(status=StatusChoices.RENDERED):
            printer.print_check(check)
