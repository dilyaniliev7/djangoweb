from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models
from djangoweb.accounts.managers import AppUserManager
from djangoweb.accounts.validators import validate_only_letters


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 5
    MAX_LEN_FIRST_NAME = 30

    MIN_LEN_LAST_NAME = 5
    MAX_LEN_LAST_NAME = 30

    MIN_DESCRIPTION_LENGTH = 5

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    profile_picture = cloudinary_models.CloudinaryField(
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=40,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        null=True,
        blank=True,
    )
