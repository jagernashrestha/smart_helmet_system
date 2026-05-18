from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Rider
from .forms import RiderForm

@login_required
def rider_list(request):
    riders = Rider.objects.all().order_by('name')
    return render(request, 'riders/rider_list.html', {'riders': riders})

@login_required
def rider_add(request):
    if request.method == 'POST':
        form = RiderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rider added successfully!')
            return redirect('rider_list')
    else:
        form = RiderForm()
    return render(request, 'riders/rider_form.html', {'form': form, 'title': 'Add Rider'})

@login_required
def rider_edit(request, pk):
    rider = get_object_or_404(Rider, pk=pk)
    if request.method == 'POST':
        form = RiderForm(request.POST, instance=rider)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rider updated!')
            return redirect('rider_list')
    else:
        form = RiderForm(instance=rider)
    return render(request, 'riders/rider_form.html', {'form': form, 'title': 'Edit Rider'})

@login_required
def rider_delete(request, pk):
    rider = get_object_or_404(Rider, pk=pk)
    if request.method == 'POST':
        rider.delete()
        messages.success(request, 'Rider deleted.')
        return redirect('rider_list')
    return render(request, 'riders/rider_confirm_delete.html', {'rider': rider})
