import mimetypes
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import json
from base64 import b64encode

from .models import Hotel, Beach, HotelAndBeachReservation

from .forms import ReservationForm


def serve_image(request, image_file):
    # Get the absolute path to the image file
    image_path = os.path.join(settings.STATIC_ROOT, 'images', image_file)

    try:
        with open(image_path, 'rb') as f:
            # Read the image file
            image_data = f.read()
            # Determine the content type based on the file extension
            content_type, _ = mimetypes.guess_type(image_path)
            # Set the appropriate content type
            if content_type is None:
                content_type = 'application/octet-stream'
            # Return the image as a response
            return HttpResponse(image_data, content_type=content_type)
    except FileNotFoundError:
        # Return a 404 error if the image file is not found
        return HttpResponse(status=404)


def beachesAndHotels(request):
    hotels = Hotel.objects.all()
    beaches = Beach.objects.all()

    for hotel in hotels:
        hotel.description_short = hotel.description[:155]
        if len(hotel.description) > 50:
            hotel.description_short += "..."
        image_data = hotel.image.read()
        hotel.image_data = b64encode(image_data).decode('utf-8')

    for beach in beaches:
        beach.description_short = beach.description[:155]
        if len(beach.description) > 50:
            beach.description_short += "..."
        image_data = beach.image.read()
        beach.image_data = b64encode(image_data).decode('utf-8')

    context = {'beaches': beaches, 'hotels': hotels}

    return render(request, 'beaches-and-hotel.html', context)


def beach_details(request, beach_id):
    beach = get_object_or_404(Beach, id=beach_id)

    context = {
        'beach': beach,
    }

    return render(request, 'beach-details.html', context)


@csrf_exempt
def reservation_beach_view(request, beach_id):
    beach = Beach.objects.get(id=beach_id)
    image_data = beach.image.read()
    beach.image_data = b64encode(image_data).decode('utf-8')

    if request.method == 'POST':
        # Get the data from the request body
        data = json.loads(request.body)
        # Extract the customer information
        beachId = data.get('beach')
        name = data.get('name')
        email = data.get('email')
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        beach = Beach.objects.get(id=beachId)

        try:
            # Save the customer to the database with the book foreign key
            reserve = HotelAndBeachReservation(
                beach=beach, name=name, email=email, check_in_date=check_in_date, check_out_date=check_out_date)
            reserve.save()

            # Return a success response
            return JsonResponse({'message': 'Customer information saved successfully.'})

        except Beach.DoesNotExist:
            # Return an error response if the book does not exist
            return JsonResponse({'error': 'Book does not exist.'}, status=400)

    else:
        form = ReservationForm()

    context = {
        'beach': beach,
        'form': form,
    }

    return render(request, 'reservation.html', context)


def beaches(request):
    return render(request, 'beaches.html')


def hotels(request):
    return render(request, 'hotels.html')
