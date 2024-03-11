from django.urls import path, include

from djangoweb.djangogram.views import index, like_functionality

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_functionality, name='like photo'),
)
