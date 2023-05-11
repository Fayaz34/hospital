from django import forms
from .models import Booking


class dateInput(forms.DateInput):
    input_type = 'date'


class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': dateInput(),
        }