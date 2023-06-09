from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.beachesAndHotels, name='beaches-and-hotels'),
    path('reservation/<int:beach_id>/', views.reservation_beach_view, name='reservation'),
    path('beaches', views.beaches, name='beaches'),
    path('beach-details/<int:beach_id>/', views.beach_details, name='beach-details'),
    path('hotels', views.hotels, name='hotels'),
    path('beach_images/<str:image_file>',
         views.serve_image, name='beach_image'),
   path('hotel_images/<str:image_file>', views.serve_image, name='hotel_image'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
