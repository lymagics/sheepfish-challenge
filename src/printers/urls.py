from rest_framework.routers import DefaultRouter

from .api.views import PrinterViewSet

router = DefaultRouter()
router.register('printers', PrinterViewSet, basename='printers')
urlpatterns = router.urls

app_name = 'printers'
