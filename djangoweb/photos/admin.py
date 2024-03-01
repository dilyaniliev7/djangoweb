from django.contrib import admin

from djangoweb.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'location', 'publication_date')