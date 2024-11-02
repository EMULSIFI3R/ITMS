from django import forms
from .models import FakeTaxi, Driver, Vehicle

class FakeTaxiForm(forms.ModelForm):
    class Meta:
        model = FakeTaxi
        fields = ['vehicle', 'driver', 'license_plate', 'color', 'capacity', 'available']  # Removed 'model'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.all()
        self.fields['driver'].queryset = Driver.objects.all()
