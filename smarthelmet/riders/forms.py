from django import forms
from .models import Rider

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name', 'phone', 'emergency_contact_name', 'emergency_contact_phone', 'helmet_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+977-XXXXXXXXXX'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Name'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+977-XXXXXXXXXX'}),
            'helmet_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. H001'}),
        }
