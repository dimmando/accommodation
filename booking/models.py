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

    ACCOMMODATION_TYPES = [
        ('Room', 'Room'),
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
    ]

    post_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_posts'
    )

    title = models.CharField(max_length=50)
    description = models.TextField()
    accommodation_type = models.CharField(max_length=10, choices=ACCOMMODATION_TYPES)
    city = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=0)
    booking_image = CloudinaryField('booking_image', default='placeholder')
    owner_email = models.EmailField()
    owner_phone = PhoneNumberField(region="IE")

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)

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
