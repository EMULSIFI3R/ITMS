from django.db import models
import os
from django.conf import settings

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model_name}"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    nfc_code = models.CharField(max_length=255, blank=True, null=True, unique=True)  # Add unique constraint

    def __str__(self):
        return self.name

class FakeTaxi(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Direct reference without string
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)  # Direct reference without string
    license_plate = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def clear_qr_code(self):
        """Method to clear the QR code."""
        if self.qr_code:
            if os.path.isfile(self.qr_code.path):
                os.remove(self.qr_code.path)  # Delete the file from filesystem
            self.qr_code = None
            self.save()