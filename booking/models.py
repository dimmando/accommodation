from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Accommodation(models.Model):
    """
    Accommodation Model
    """
    ACCOMMODATION_TYPES = [
        ('Flat', 'Flat'),
        ('Room', 'Room'),
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    accommodation_type = models.CharField(
        max_length=20, choices=ACCOMMODATION_TYPES, default='Flat')
    accommodation_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    number_of_guests = models.IntegerField(default=1)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.accommodation.name} by {self.user.username}"