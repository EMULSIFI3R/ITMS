from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from .models import FakeTaxi
from .serializers import FakeTaxiSerializer
import qrcode
import io
from django.core.files.base import ContentFile
from django.http import HttpResponse, JsonResponse
from .forms import FakeTaxiForm
from django.contrib import messages
from rest_framework.views import APIView
from .models import Driver
import logging

logger = logging.getLogger(__name__)

class FakeTaxiListCreateView(generics.ListCreateAPIView):
    queryset = FakeTaxi.objects.all()
    serializer_class = FakeTaxiSerializer

class GenerateQRCodeView(generics.GenericAPIView):
    def get(self, request, license_plate):
        try:
            taxi = FakeTaxi.objects.get(license_plate=license_plate)
        except FakeTaxi.DoesNotExist:
            return Response({"error": "Taxi not found"}, status=404)

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(taxi.license_plate)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buf = io.BytesIO()
        img.save(buf)
        buf.seek(0)

        return HttpResponse(buf.getvalue(), content_type='image/png')

def add_fake_taxi(request):
    if request.method == 'POST':
        form = FakeTaxiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fake taxi added successfully!')
            return redirect('add_fake_taxi')  # Redirect to the same page or another page
    else:
        form = FakeTaxiForm()
    
    return render(request, 'add_fake_taxi.html', {'form': form})

class GenerateQRCodeView(APIView):
    def get(self, request, id):  # Changed from license_plate to id
        try:
            taxi = FakeTaxi.objects.get(id=id)  # Fetch by ID instead of license_plate
        except FakeTaxi.DoesNotExist:
            return Response({"error": "Taxi not found"}, status=404)

        # Generate the URL with the taxi's ID
        form_url = f"https://example.com/form?id={taxi.id}"

        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(form_url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buf = io.BytesIO()
        img.save(buf)
        buf.seek(0)

        return HttpResponse(buf.getvalue(), content_type='image/png')

def add_fake_taxi(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'passenger':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            remarks = request.POST.get('remarks')
            email = request.POST.get('email')
            # Process passenger data (save to DB or other logic)
            messages.success(request, 'Passenger form submitted successfully!')
        elif user_type == 'officer':
            officer_id = request.POST.get('officer_id')
            name = request.POST.get('name')
            contact = request.POST.get('contact')
            office = request.POST.get('office')
            location = request.POST.get('location')
            # Process officer data
            messages.success(request, 'Officer form submitted successfully!')
        return redirect('vehicle_form')

    return render(request, 'form.html')

def get_driver_info(request, nfc_code):
    logger.debug(f"Fetching driver info for NFC code: {nfc_code}")
    try:
        driver = Driver.objects.get(nfc_code=nfc_code)
        data = {
            'name': driver.name,
            'license_number': driver.license_number,
            'nfc_code': driver.nfc_code,
        }
        logger.debug(f"Driver found: {data}")
        return JsonResponse(data)
    except Driver.DoesNotExist:
        logger.debug(f"Driver with NFC code {nfc_code} not found")
        return JsonResponse({'error': 'Driver not found'}, status=404)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return JsonResponse({'error': 'An error occurred'}, status=500)
