from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from riders.models import Rider
from accidents.models import Helmet, Accident
from django.utils import timezone

@login_required
def home(request):
    total_helmets = Helmet.objects.count()
    active_riders = Helmet.objects.filter(status='safe').count()
    today = timezone.now().date()
    accidents_today = Accident.objects.filter(timestamp__date=today).count()
    unresolved_accidents = Accident.objects.filter(resolved=False).count()
    gps_connected = Helmet.objects.filter(gps_active=True).count()

    recent_accidents = Accident.objects.select_related('helmet', 'helmet__rider').filter(resolved=False)[:5]

    context = {
        'total_helmets': total_helmets,
        'active_riders': active_riders,
        'accidents_today': accidents_today,
        'unresolved_accidents': unresolved_accidents,
        'gps_connected': gps_connected,
        'recent_accidents': recent_accidents,
    }
    return render(request, 'dashboard/home.html', context)
