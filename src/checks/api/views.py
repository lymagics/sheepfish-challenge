from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CheckSerializer
from ..models import Check


class CheckViewSet(viewsets.ModelViewSet):
    """
    DRF Check viewset.
    """
    http_method_names = ('get', 'post',)
    serializer_class = CheckSerializer

    def get_queryset(self):
        return Check.objects.select_related('printer')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({}, status=201)
