from django.db import models

class Beach(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    location = models.CharField(max_length=100, default='Argao, Cebu')
    image = models.ImageField(upload_to='beach_images',
                              default='default_image.jpg')
    facilities = models.TextField()
    activities = models.TextField()
    room_types = models.TextField(default="")
    amenities = models.TextField(default="")

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    location = models.CharField(max_length=100, default='Argao, Cebu')
    image = models.ImageField(upload_to='hotel_images',
                              default='default_image.jpg')
    amenities = models.TextField(default="")
    room_types = models.TextField(default="")

    def __str__(self):
        return self.name


class HotelAndBeachReservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    beach = models.ForeignKey(
        Beach, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Reservation #{self.id} - {self.name}"
