from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('hotels/', views.hotels, name='hotels'),
    path('beaches/', views.beaches, name='beaches'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
