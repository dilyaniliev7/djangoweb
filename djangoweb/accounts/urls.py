from django.urls import path, include
from djangoweb.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailView, UserEditView, \
    ProfileDeleteView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete profile'),
    ])),
)

from .signals import *