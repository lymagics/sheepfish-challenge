from rest_framework.serializers import ModelSerializer

from ..models import Printer


class PrinterSerializer(ModelSerializer):
    """
    DRF serializer to represent Printer model.
    """
    class Meta:
        model = Printer
        fields = ('pk', 'name', 'api_key', 'check_type', 'point_id',)
        read_only_fields = ('pk',)
