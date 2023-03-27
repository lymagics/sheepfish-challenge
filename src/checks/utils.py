import json
import base64

from django.conf import settings
from django.template.loader import render_to_string
from django.core.files.base import ContentFile

import requests

from .models import Check


def html_to_pdf(check: Check):
    """
    Convert html to pdf with wkhtmltopdf service.
    """
    html_order = render_to_string('check.html', {'check': check})
    encoded_order = _encode_order(html_order)
    response = _send_request(encoded_order)
    return ContentFile(response.content)


def _encode_order(html_order: str) -> bytes:
    """
    Encode order to base64.
    """
    return base64.b64encode(bytes(html_order, 'utf-8'))


def _send_request(encoded_order: bytes) -> requests.Response:
    """
    Send order to wkhtmltopdf service.
    """
    data = {
        'contents': encoded_order.decode('utf-8'),
    }
    headers = {
        'Content-Type': 'application/json',
    }

    return requests.post(settings.WKHTMLTOPDF_URL, data=json.dumps(data), headers=headers)
