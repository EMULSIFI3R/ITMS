from django.urls import path
from .views import FakeTaxiListCreateView, GenerateQRCodeView, add_fake_taxi

urlpatterns = [
    path('faketaxis/', FakeTaxiListCreateView.as_view(), name='faketaxi-list-create'),
    path('faketaxis/qrcode/<str:license_plate>/', GenerateQRCodeView.as_view(), name='generate-qrcode'),
    path('add_fake_taxi/', add_fake_taxi, name='add_fake_taxi'),
    path('generate_qr/<str:license_plate>/', GenerateQRCodeView.as_view(), name='generate_qr'),
    path('form/', add_fake_taxi, name='vehicle_form'),

]
