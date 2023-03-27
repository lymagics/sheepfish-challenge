from django.contrib import admin

from .models import Printer


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    """
    Django admin model to represent Printer model.
    """
    list_display = ('name', 'check_type', 'point_id',)
