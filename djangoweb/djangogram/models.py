from django.contrib.auth import get_user_model
from django.db import models

from djangoweb.photos.models import Photo

UserModel = get_user_model()


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

