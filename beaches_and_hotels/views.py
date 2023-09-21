import mimetypes
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import json
from base64 import b64encode

from .models import Hotel, Beach, HotelAndBeachReservation, HotelAndBeachRoomType

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


@csrf_exempt
def hotel_beach_details_json(request, beach_id):
    try:
        beach = Beach.objects.get(id=beach_id)
        image_data = beach.image.read()
        beach.image_data = b64encode(image_data).decode('utf-8')

         # Convert the beach object to a dictionary
        beach_data = {
            'id': beach.id,
            'name': beach.name,
            'image_data': beach.image_data
            # Include other beach fields as needed
        }
        
        # Build the response JSON object
        response = {
            'beach': beach_data,
        }

        return JsonResponse(response)
    except Beach.DoesNotExist:
        try:
            hotel = Hotel.objects.get(id=beach_id)
            image_data = hotel.image.read()
            hotel.image_data = b64encode(image_data).decode('utf-8')

            beach_data = {
            'id': hotel.id,
            'name': hotel.name,
            'image_data': hotel.image_data
            # Include other hotel fields as needed
            }
        
            # Build the response JSON object
            response = {
                'beach': beach_data,
            }
            return JsonResponse(response)
        except Hotel.DoesNotExist:
            # Handle the case when neither Beach nor Hotel object is found
            return HttpResponse('No Beach or Hotel found.')

def hotel_beach_details(request, beach_id):
    try:
        beach = Beach.objects.get(id=beach_id)
        room_types = beach.hotelandbeachroomtype_set.all()
        image_data = beach.image.read()
        beach.image_data = b64encode(image_data).decode('utf-8')

        context = {
            'room_types': room_types,
            'beach': beach,
        }

        return render(request, 'beach-hotel-details.html', context)
    except Beach.DoesNotExist:
        try:
            hotel = Hotel.objects.get(id=beach_id)
            room_types = hotel.hotelandbeachroomtype_set.all()
            image_data = hotel.image.read()
            hotel.image_data = b64encode(image_data).decode('utf-8')

            context = {
                'beach': hotel,
                'room_types': room_types,
            }

            return render(request, 'beach-hotel-details.html', context)
        except Hotel.DoesNotExist:
            # Handle the case when neither Beach nor Hotel object is found
            return HttpResponse('No Beach or Hotel found.')


@csrf_exempt
def reservation_beach_view(request, beach_id):
    hotel = None
    beach = None
    room_type = None
    try:
        beach = Beach.objects.get(id=beach_id)
        image_data = beach.image.read()
        beach.image_data = b64encode(image_data).decode('utf-8')
    except Beach.DoesNotExist:
        try:
            hotel = Hotel.objects.get(id=beach_id)
            image_data = hotel.image.read()
            hotel.image_data = b64encode(image_data).decode('utf-8')
        except Hotel.DoesNotExist:
            return JsonResponse({'error': 'Invalid beach or hotel ID.'}, status=400)

    if request.method == 'POST':
        data = json.loads(request.body)
        number_of_guests = data.get('number_of_guests')
        name = data.get('name')
        email = data.get('email')
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        try:
            room_type_id = data.get('room_type')
            room_type = HotelAndBeachRoomType.objects.get(id=room_type_id)
        except HotelAndBeachRoomType.DoesNotExist:
            # Handle the case when the room type does not exist
            room_type = None

        try:
            reserve = HotelAndBeachReservation(
                beach=beach or None,
                name=name,
                email=email,
                room_type=room_type or None,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                hotel=hotel or None,
                number_of_guests=number_of_guests
            )
            reserve.save()
            return JsonResponse({'message': 'Customer information saved successfully.'})
        except Beach.DoesNotExist:
            return JsonResponse({'error': 'Beach does not exist.'}, status=400)

    else:
        form = ReservationForm()

    context = {
        'beach': beach,
        'form': form,
    }

    return render(request, 'reservation.html', context)
