from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from djangoweb.djangogram.models import PhotoLike
from djangoweb.djangogram.utils import get_photo_url
from djangoweb.photos.models import Photo

UserModel = get_user_model()


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def index(request):
    photos = Photo.objects.all()
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    user = UserModel
    context = {
        'user': UserModel,
        'photos': photos,
    }
    return render(request, 'index.html', context)


@login_required
def like_functionality(request, photo_id):
    user_liked_photos = PhotoLike.objects.filter(to_photo_id=photo_id, user_id=request.user.pk)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            to_photo_id=photo_id,
            user_id=request.user.pk,
        )
    return redirect(get_photo_url(request, photo_id))


