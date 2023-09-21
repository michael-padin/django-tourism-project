from django import forms
from .models import HotelAndBeachReservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = HotelAndBeachReservation
        fields = ['check_in_date', 'check_out_date',
                  'beach', 'hotel', 'name', 'email']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }
