from django.urls import path, include

urlpatterns = [
    path('', include('printers.urls')),
    path('', include('checks.urls')),
]

app_name = 'api'
