# Generated by Django 4.2.2 on 2023-06-09 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beaches_and_hotels', '0008_alter_beach_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='beach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beaches_and_hotels.beach'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beaches_and_hotels.hotel'),
        ),
    ]
