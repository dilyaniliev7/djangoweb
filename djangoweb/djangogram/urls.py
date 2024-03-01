from django.urls import path, include

from djangoweb.djangogram.views import index

urlpatterns = (
    path('', index, name='index'),
)
