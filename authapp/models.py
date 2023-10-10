from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    detailed_address = models.TextField(null=True, blank=True)
    id_proof_choices = [
        ('aadharcard', 'Aadhar Card'),
        ('pancard', 'PAN Card'),
        ('other', 'Other'),
    ]
    id_proof = models.CharField(max_length=20, choices=id_proof_choices, null=True, blank=True)
    id_proof_upload = models.FileField(upload_to='id_proofs/', null=True, blank=True)
    country = models.CharField(max_length=100, default="India")
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
