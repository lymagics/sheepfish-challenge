from django.db import models


class TypeChoices(models.TextChoices):
    """
    The type of check printed by the printer.
    """
    KITCHEN = 'kitchen', 'Kitchen'
    CLIENT = 'client', 'Client'


class StatusChoices(models.TextChoices):
    """
    Check status.
    """
    NEW = 'new', 'New'
    RENDERED = 'rendered', 'Rendered'
    PRINTED = 'printed', 'Printed'
