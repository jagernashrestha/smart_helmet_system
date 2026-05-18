from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.receive_sensor_data, name='receive_data'),
    path('status/', views.latest_status, name='latest_status'),
]
