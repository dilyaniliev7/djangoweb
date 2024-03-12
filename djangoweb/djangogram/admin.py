from django.contrib import admin

from djangoweb.djangogram.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
