# Generated by Django 4.2.9 on 2024-07-21 15:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
