# Generated by Django 4.2.2 on 2023-06-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beaches_and_hotels', '0007_remove_reservation_tour_package_reservation_beach_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beach',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='beach_images'),
        ),
    ]