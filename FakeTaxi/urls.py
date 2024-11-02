from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from taxi.views import get_driver_info  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('taxi.urls')),
    path('nfc/', TemplateView.as_view(template_name='NFC.html'), name='nfc'),
    path('driver-info/<str:nfc_code>/', get_driver_info, name='get_driver_info'),  # Add this line
]
