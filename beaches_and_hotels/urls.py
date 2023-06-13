from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.beachesAndHotels, name='beaches-and-hotels'),
    path('hotel-beach-details/<int:beach_id>/', views.hotel_beach_details, name='hotel-beach-details'),
    path('hotel-beach-details-json/<int:beach_id>/', views.hotel_beach_details_json, name='hotel-beach-details-json'),
    path('reservation/<int:beach_id>/', views.reservation_beach_view, name='reservation'),
    path('beach_images/<str:image_file>',
         views.serve_image, name='beach_image'),
   path('hotel_images/<str:image_file>', views.serve_image, name='hotel_image'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
