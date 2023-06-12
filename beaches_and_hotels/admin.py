from django.contrib import admin
from .models import Beach, Hotel, HotelAndBeachReservation

admin.site.register(Beach)
admin.site.register(Hotel)
admin.site.register(HotelAndBeachReservation)
