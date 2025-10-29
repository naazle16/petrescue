from django.db import models
from django.contrib.auth.models import User

class FoundPet(models.Model):
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50, choices=PET_TYPES)
    location_found = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='found_pets/')
    status = models.CharField(max_length=20, default='Pending')
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet_name} ({self.status})"
