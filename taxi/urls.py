from django.urls import path
from django.views.generic import TemplateView
from .views import FakeTaxiListCreateView, GenerateQRCodeView, add_fake_taxi
from . import views

urlpatterns = [
    path('faketaxis/', FakeTaxiListCreateView.as_view(), name='faketaxi-list-create'),
    path('faketaxis/qrcode/<str:license_plate>/', GenerateQRCodeView.as_view(), name='generate-qrcode'),
    path('add_fake_taxi/', add_fake_taxi, name='add_fake_taxi'),
    path('generate_qr/<str:license_plate>/', GenerateQRCodeView.as_view(), name='generate_qr'),
    path('form/', add_fake_taxi, name='vehicle_form'),
    path('driver-info/<str:nfc_code>/', views.get_driver_info, name='get_driver_info'),
    path('nfc/', TemplateView.as_view(template_name='NFC.html'), name='nfc'),

]
