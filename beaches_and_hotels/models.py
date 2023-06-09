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


class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    image = models.ImageField(
        upload_to='package_images', default='default_image.jpg')
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reservation(models.Model):
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


class BeachRoomType(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class HotelRoomType(models.Model):
    beach = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
