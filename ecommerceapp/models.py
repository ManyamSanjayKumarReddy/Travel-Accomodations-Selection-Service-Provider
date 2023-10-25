from django.db import models
from django.contrib.auth.models import User
import json

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.IntegerField()

    def __str__(self):
        return self.name

class RoomType(models.Model):
    room_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    vacancies = models.PositiveIntegerField(default=0)
    has_food_facility = models.BooleanField(default=False)
    has_swimming_pool = models.BooleanField(default=False)
    near_airport = models.BooleanField(default=False)
    sea_area = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/images', default="")
    image1 = models.ImageField(upload_to='images/additional-images', default="")
    image2 = models.ImageField(upload_to='images/additional-images', default="")
    image3 = models.ImageField(upload_to='images/additional-images', default="")
    image4 = models.ImageField(upload_to='images/additional-images', default="")
    image5 = models.ImageField(upload_to='images/additional-images', default="")
    image6 = models.ImageField(upload_to='images/additional-images', default="")

    def __str__(self):
        return self.room_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    appointment_date = models.DateField(null=True, blank=True)
    updated_appointment_date = models.DateField(null=True, blank=True)
    id_proof = models.ImageField(upload_to='id_proofs/', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    aadhar = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return self.name

class Rating(models.Model):
    room = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.pk} for {self.room.room_name} by {self.user.username} ({self.rating})"
