from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Accident, Helmet

@login_required
def accident_list(request):
    accidents = Accident.objects.select_related('helmet', 'helmet__rider').all()
    unresolved = accidents.filter(resolved=False)
    resolved = accidents.filter(resolved=True)
    return render(request, 'accidents/accident_list.html', {
        'unresolved': unresolved,
        'resolved': resolved,
    })

@login_required
def accident_detail(request, pk):
    accident = get_object_or_404(Accident, pk=pk)
    return render(request, 'accidents/accident_detail.html', {'accident': accident})

@login_required
def accident_resolve(request, pk):
    accident = get_object_or_404(Accident, pk=pk)
    accident.resolved = True
    accident.save()
    messages.success(request, f'Accident #{pk} marked as resolved.')
    return redirect('accident_list')

@login_required
def helmet_status(request):
    helmets = Helmet.objects.select_related('rider').all()
    return render(request, 'accidents/helmet_status.html', {'helmets': helmets})
