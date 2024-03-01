from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from djangoweb.photos.forms import PhotoCreateForm
from djangoweb.photos.models import Photo


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    context = {
        'photo': photo,

    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request):
    pass


def delete_photo(request):
    pass