from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.utils.text import slugify
from autoslug import AutoSlugField

from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.html import mark_safe
from django.contrib import admin

from django.templatetags.static import static


class BookPost(models.Model):
    """
    Model to store user's data that they input into the form when create
    their own property that would like to propose for guest's accommodation
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

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=600, null=False, blank=False)
    accommodation_type = models.CharField(max_length=10, choices=ACCOMMODATION_TYPES)
    city = models.CharField(max_length=100, null=False, blank=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    booking_image = CloudinaryField('booking_image', default='placeholder')
    owner_email = models.EmailField(max_length=100, null=False, blank=False)
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
        for the property they just posted.
        https://www.youtube.com/watch?v=-s7e_Fy6NRU
        https://ngangasn.com/what-is-get_absolute_url-in-django/
        """
        return reverse('book_detail', args=[str(self.slug)])

    def image_tag(self):
        if 'placeholder' in self.booking_image.url:
            placeholder_url = static('images/default.png')
            return mark_safe(f'<img src="{placeholder_url}" width="150" height="150" alt="Placeholder Image" />')
        return mark_safe(f'<img src="{self.booking_image.url}" width="150" height="150" />')

        # if self.booking_image:
        #     return mark_safe(f'<img src="{self.booking_image.url}" width="150" height="150" />')
        # return "No Image"

    image_tag.short_description = 'Image Preview'

