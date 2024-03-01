from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from djangoweb.photos.validators import validate_file_less_than_5mb

UserModel = get_user_model()


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='mediafiles/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
