from django.contrib import admin

from .models import Check


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    """
    Django admin model to represent Check model.
    """
    list_display = ('pk', 'check_type', 'status', 'printer',)
