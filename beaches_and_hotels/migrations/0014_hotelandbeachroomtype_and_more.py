# Generated by Django 4.2 on 2023-06-12 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beaches_and_hotels', '0013_alter_beach_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelAndBeachRoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('beach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beaches_and_hotels.beach')),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beaches_and_hotels.hotel')),
            ],
        ),
        migrations.AlterField(
            model_name='hotelandbeachreservation',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beaches_and_hotels.hotelandbeachroomtype'),
        ),
        migrations.DeleteModel(
            name='HotelRoomType',
        ),
    ]
