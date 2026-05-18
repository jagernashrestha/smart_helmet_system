from django.contrib import admin
from .models import Helmet, SensorData, Accident
admin.site.register(Helmet)
admin.site.register(SensorData)
admin.site.register(Accident)
