from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from djangoweb.photos.models import Photo

UserModel = get_user_model()


def index(request):
    photos = Photo.objects.all()
    user = UserModel
    context = {
        'user': UserModel,
        'photos': photos,
    }
    return render(request, 'index.html', context)

