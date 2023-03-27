from rest_framework import viewsets

from .serializers import PrinterSerializer
from ..models import Printer


class PrinterViewSet(viewsets.ModelViewSet):
    """
    DRF Printer viewset.
    """
    http_method_names = ('get', 'post',)
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()
