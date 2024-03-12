from django.urls import path, include

from djangoweb.djangogram.views import index, like_functionality, comment_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_functionality, name='like photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo')
)
