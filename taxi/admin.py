from django.contrib import admin
from .models import Vehicle, Driver, FakeTaxi
import qrcode
from django.core.files.base import ContentFile
import io
from django.urls import reverse

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model_name', 'year')  # Adjust fields as necessary
    search_fields = ('make', 'model_name', 'year')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'license_number', 'nfc_code')  # Add nfc_code to display
    search_fields = ('name', 'license_number', 'nfc_code')  # Add nfc_code to search fields

@admin.register(FakeTaxi)
class FakeTaxiAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'driver', 'license_plate', 'color', 'capacity', 'available', 'view_qr_code')  # Adjust fields as necessary
    search_fields = ('license_plate', 'vehicle__make', 'driver__name')  # Allows searching by related fields
    actions = ['generate_qr_code', 'clear_qr_code']

    def clear_qr_code(self, request, queryset):
        """Action to clear the QR codes for the selected FakeTaxi objects."""
        for taxi in queryset:
            taxi.clear_qr_code()  # Call the method to clear the QR code
        self.message_user(request, "QR codes cleared successfully.")

    clear_qr_code.short_description = "Clear QR Code for selected FakeTaxis"
    
    def view_qr_code(self, obj):
        """Show a link to the QR code if it exists."""
        if obj.qr_code:
            return f'<a href="{obj.qr_code.url}" target="_blank">View QR Code</a>'
        return "QR Code not generated"
    view_qr_code.allow_tags = True  # To render HTML in Django Admin
    view_qr_code.short_description = 'QR Code'

    def generate_qr_code(self, request, queryset):
        """Generate QR codes for the selected FakeTaxi objects."""
        for taxi in queryset:
            # Generate the URL containing the ID of the FakeTaxi
            form_url = f"https://your-domain.com/form?id={taxi.id}"

            # Generate the QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(form_url)
            qr.make(fit=True)

            # Save the QR code to an in-memory buffer
            img = qr.make_image(fill='black', back_color='white')
            buf = io.BytesIO()
            img.save(buf)
            buf.seek(0)

            # Save the QR code to the model's ImageField
            filename = f"{taxi.id}_qr.png"
            taxi.qr_code.save(filename, ContentFile(buf.getvalue()), save=True)

        self.message_user(request, "QR codes generated successfully.")

    generate_qr_code.short_description = "Generate QR Code for selected FakeTaxis"
