from django import forms
from .models import FoundPet

class FoundPetForm(forms.ModelForm):
    class Meta:
        model = FoundPet
        fields = ['pet_name', 'pet_type', 'location_found', 'description', 'image']
        widgets = {
            'pet_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pet name'}),
            'pet_type': forms.Select(attrs={'class': 'form-select'}),
            'location_found': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Where was the pet found?'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the pet'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
