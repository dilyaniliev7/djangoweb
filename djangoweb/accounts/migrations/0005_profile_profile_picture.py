# Generated by Django 4.2.9 on 2024-04-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_appuser_managers_alter_appuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles/profile_pictures/'),
        ),
    ]
