from django.contrib import admin
from .models import Beach, Hotel, TourPackage, Reservation, HotelRoomType, BeachRoomType, RoomType

admin.site.register(Beach)
admin.site.register(Hotel)
admin.site.register(TourPackage)
admin.site.register(Reservation)
admin.site.register(HotelRoomType)
admin.site.register(BeachRoomType)
admin.site.register(RoomType)
