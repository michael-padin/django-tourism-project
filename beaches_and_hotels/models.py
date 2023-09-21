from django.db import models


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

    def get_amenities_list(self):
        return self.amenities.split(",") if self.amenities else []

    def set_amenities_list(self, amenities_list):
        self.amenities = ",".join(amenities_list)

    amenities_list = property(get_amenities_list, set_amenities_list)


class Beach(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    location = models.CharField(max_length=100, default='Argao, Cebu')
    image = models.ImageField(upload_to='beach_images',
                              default='default_image.jpg')
    amenities = models.TextField(default="")
    def __str__(self):
        return self.name
    

    def get_amenities_list(self):
        return self.amenities.split(",") if self.amenities else []

    def set_amenities_list(self, amenities_list):
        self.amenities = ",".join(amenities_list)

    amenities_list = property(get_amenities_list, set_amenities_list)


class HotelAndBeachRoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE,  null=True, blank=True)
    beach = models.ForeignKey(
        Beach, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        if self.beach:
            return f"{self.beach.name} - {self.name}"
        elif self.hotel:
            return f"{self.hotel.name} - {self.name}"
        else:
            return self.name


class HotelAndBeachReservation(models.Model):
    beach = models.ForeignKey(
        Beach, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, null=True, blank=True)
    room_type = models.ForeignKey(
        HotelAndBeachRoomType, on_delete=models.CASCADE, null=True, blank=True)
    number_of_guests = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation #{self.id} - {self.name}"
