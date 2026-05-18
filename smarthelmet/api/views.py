import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from accidents.models import Helmet, SensorData, Accident

@csrf_exempt
def receive_sensor_data(request):
    """
    ESP32 sends POST request to /api/data/ with JSON body.

    Example JSON from ESP32:
    {
        "helmet_id": "H001",
        "acceleration": 12.5,
        "tilt": 45.0,
        "latitude": 27.7172,
        "longitude": 85.3240,
        "helmet_worn": true,
        "accident": false,
        "battery": 85
    }
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    helmet_id = data.get('helmet_id')
    if not helmet_id:
        return JsonResponse({'error': 'helmet_id is required'}, status=400)

    # Get or create the helmet
    helmet, created = Helmet.objects.get_or_create(
        helmet_id=helmet_id,
        defaults={'status': 'safe'}
    )

    # Update battery and GPS status
    helmet.battery = data.get('battery', helmet.battery)
    helmet.gps_active = bool(data.get('latitude'))

    is_accident = data.get('accident', False)

    if is_accident:
        helmet.status = 'accident'
    elif data.get('helmet_worn', True):
        helmet.status = 'safe'
    else:
        helmet.status = 'offline'

    helmet.save()

    # Save sensor data log
    SensorData.objects.create(
        helmet=helmet,
        acceleration=data.get('acceleration', 0),
        tilt=data.get('tilt', 0),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        helmet_worn=data.get('helmet_worn', True),
    )

    # Create accident record if accident detected
    if is_accident:
        Accident.objects.create(
            helmet=helmet,
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            location_description=data.get('location', 'Unknown Location'),
            severity=data.get('severity', 'medium'),
        )

    return JsonResponse({'status': 'ok', 'message': 'Data received successfully'})


def latest_status(request):
    """
    Dashboard polls this every 5 seconds to get live updates.
    Returns JSON with latest helmet statuses and accident count.
    """
    helmets = Helmet.objects.select_related('rider').all()
    helmet_data = []
    for h in helmets:
        helmet_data.append({
            'helmet_id': h.helmet_id,
            'status': h.status,
            'battery': h.battery,
            'gps_active': h.gps_active,
            'rider_name': h.rider.name if h.rider else 'Unassigned',
            'last_seen': h.last_seen.strftime('%Y-%m-%d %H:%M:%S'),
        })

    unresolved_accidents = Accident.objects.filter(resolved=False).count()

    # Get latest unresolved accident for alert popup
    latest_accident = Accident.objects.filter(resolved=False).first()
    alert = None
    if latest_accident:
        alert = {
            'id': latest_accident.pk,
            'helmet_id': latest_accident.helmet.helmet_id,
            'rider': latest_accident.helmet.rider.name if latest_accident.helmet.rider else 'Unknown',
            'latitude': latest_accident.latitude,
            'longitude': latest_accident.longitude,
            'location': latest_accident.location_description,
            'severity': latest_accident.severity,
            'time': latest_accident.timestamp.strftime('%I:%M %p'),
        }

    return JsonResponse({
        'helmets': helmet_data,
        'unresolved_accidents': unresolved_accidents,
        'latest_alert': alert,
    })
