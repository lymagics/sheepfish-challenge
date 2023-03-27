from django.db.transaction import atomic

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Check
from ..tasks import create_pdf_file
from printers.api.serializers import PrinterSerializer
from printers.models import Printer


class CheckSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent Check model.
    """
    printer = PrinterSerializer(read_only=True)
    point_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Check
        fields = ('pk', 'check_type', 'status', 'printer', 'order', 'point_id')
        read_only_fields = ('pk',)

    @atomic
    def create(self, validated_data):
        point_id = validated_data.pop('point_id')
        check_type = validated_data['check_type']

        printers = Printer.objects.filter(point_id=point_id, check_type=check_type)

        if not printers:
            error = 'No available printers'
            raise ValidationError({'error': error})

        for printer in printers:
            check = Check.objects.create(
                printer=printer, **validated_data
            )
            create_pdf_file.delay(check.pk)

        return {}
