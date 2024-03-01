from django.urls import path, include
from djangoweb.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailView.as_view(), name='details user'),
    ])),
)
