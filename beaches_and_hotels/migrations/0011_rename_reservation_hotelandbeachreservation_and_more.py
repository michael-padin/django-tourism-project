# Generated by Django 4.2.2 on 2023-06-10 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beaches_and_hotels', '0010_alter_reservation_beach_alter_reservation_hotel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservation',
            new_name='HotelAndBeachReservation',
        ),
        migrations.RemoveField(
            model_name='hotelroomtype',
            name='beach',
        ),
        migrations.RemoveField(
            model_name='roomtype',
            name='beach',
        ),
        migrations.RemoveField(
            model_name='tourpackage',
            name='beach',
        ),
        migrations.RemoveField(
            model_name='tourpackage',
            name='hotel',
        ),
        migrations.DeleteModel(
            name='BeachRoomType',
        ),
        migrations.DeleteModel(
            name='HotelRoomType',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
        migrations.DeleteModel(
            name='TourPackage',
        ),
    ]
