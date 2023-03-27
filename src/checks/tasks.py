from django.shortcuts import get_object_or_404

from celery import shared_task

from .models import Check
from .utils import html_to_pdf
from core.models import StatusChoices


@shared_task
def create_pdf_file(check_pk: int):
    """
    Task for pdf file creation.
    """
    check = get_object_or_404(Check, pk=check_pk)

    pdf_file = html_to_pdf(check)
    pdf_name = f'pdf/{check.pk}_{check.check_type}.pdf'

    check.pdf_file.save(pdf_name, pdf_file)
    check.status = StatusChoices.RENDERED
    check.save()
