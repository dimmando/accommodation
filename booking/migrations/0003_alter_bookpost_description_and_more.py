# Generated by Django 4.2.16 on 2024-09-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_bookpost_book_image_bookpost_booking_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpost',
            name='description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='bookpost',
            name='owner_email',
            field=models.EmailField(max_length=100),
        ),
    ]
