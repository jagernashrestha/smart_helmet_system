from django.db import models
from riders.models import Rider

class Helmet(models.Model):
    helmet_id = models.CharField(max_length=20, unique=True)
    rider = models.OneToOneField(Rider, on_delete=models.SET_NULL, null=True, blank=True)
    battery = models.IntegerField(default=100)  # percentage
    STATUS_CHOICES = [
        ('safe', 'Safe'),
        ('accident', 'Accident Detected'),
        ('offline', 'Offline'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='offline')
    gps_active = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.helmet_id


class SensorData(models.Model):
    helmet = models.ForeignKey(Helmet, on_delete=models.CASCADE, related_name='sensor_data')
    acceleration = models.FloatField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    tilt = models.FloatField(default=0.0)
    helmet_worn = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.helmet.helmet_id} @ {self.timestamp}"


class Accident(models.Model):
    helmet = models.ForeignKey(Helmet, on_delete=models.CASCADE, related_name='accidents')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location_description = models.CharField(max_length=200, default='Unknown')
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='medium')
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Accident - {self.helmet.helmet_id} at {self.timestamp}"
