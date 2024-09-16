from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.utils.text import slugify
from autoslug import AutoSlugField

from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class BookPost(models.Model):
    """
    
    """

    # COND_CHOICES = (
    #     ('as_new', 'As New'),
    #     ('fine', 'Fine'),
    #     ('v_good', 'Very Good'),
    #     ('fair', 'Fair'),
    #     ('poor', 'Poor'),
    # )

    ACCOMMODATION_TYPES = [
        ('Flat', 'Flat'),
        ('Room', 'Room'),
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
    ]

    post_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_posts'
    )

    accommodation_type = models.CharField(max_length=10, choices=ACCOMMODATION_TYPES)
    title = models.CharField(max_length=50)
    book_image = CloudinaryField('book_image', default='placeholder')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)

    owner_email = models.EmailField()
    owner_phone = PhoneNumberField(region="IE")
    description = models.TextField()
    # book_author = models.CharField(max_length=50)
    # genre = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # reserved = models.BooleanField(default=False)


    class Meta:
        # order the posts on when they were created
        # newest posts first
        ordering = ['-created_on']

    def __str__(self):
        # django docs say to define this, returns a string from the class
        return self.title

    def get_absolute_url(self):
        """
        Get absolute url to redirect the user to the page
        for the book they just posted.
        https://www.youtube.com/watch?v=-s7e_Fy6NRU
        https://ngangasn.com/what-is-get_absolute_url-in-django/
        """
        return reverse('book_detail', args=[str(self.slug)])


# class Accommodation(models.Model):
#     """
#     Accommodation Model
#     """
#     ACCOMMODATION_TYPES = [
#         ('Flat', 'Flat'),
#         ('Room', 'Room'),
#         ('Apartment', 'Apartment'),
#         ('House', 'House'),
#         ('Villa', 'Villa'),
#     ]

#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     accommodation_type = models.CharField(
#         max_length=20, choices=ACCOMMODATION_TYPES, default='Flat')
#     accommodation_image = CloudinaryField('image', default='placeholder')

#     def __str__(self):
#         return self.name


# class Booking(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=50)
#     email = models.EmailField()
#     number_of_guests = models.IntegerField(default=1)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     booking_date = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Booking for {self.accommodation.name} by {self.user.username}"