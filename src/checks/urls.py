from rest_framework.routers import DefaultRouter

from .api.views import CheckViewSet

router = DefaultRouter()
router.register('checks', CheckViewSet, basename='checks')
urlpatterns = router.urls

app_name = 'checks'
