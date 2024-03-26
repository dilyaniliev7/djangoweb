from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError, PermissionDenied
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from djangoweb.accounts.forms import UserRegistrationForm, UserEditForm
from djangoweb.djangogram.decorators import is_owner
from djangoweb.photos.models import Photo

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'login/login.html'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if 'email' in form.errors:
            raise ValidationError('Invalid Email')
        elif 'password' in form.errors:
            raise ValidationError('Password is incorrect')

        return response

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()


class SignUpView(views.CreateView):
    template_name = 'register/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
    # template_name = 'logout/logout.html'


class ProfileDetailView(LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile-details-page.html'
    model = UserModel
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        photos = Photo.objects.filter(user=self.request.user).count()
        user_photos = Photo.objects.filter(user=self.request.user).all()
        context['user_photos'] = user_photos
        context['photos_count'] = photos
        clicked_user = self.get_object()
        clicked_user_photos = Photo.objects.filter(user=clicked_user)
        photos = self.object.photo_set.prefetch_related('photolike_set')
        photos = self.object.photo_set.prefetch_related('commentlike_set')
        context['likes_count'] = [x.photolike_set.count() for x in clicked_user_photos]
        context['comments_count'] = sum(x.photocomment_set.count() for x in clicked_user_photos)
        clicked_user_photos_count = Photo.objects.filter(user=clicked_user).count()
        context['clicked_user_info'] = clicked_user
        context['clicked_user_photos'] = clicked_user_photos
        context['clicked_user_photos_count'] = clicked_user_photos_count
        return context

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(UserModel, pk=pk)


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = 'profile/profile-edit-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        return context

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            raise Http404("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     if obj.email != self.request.user:
    #         raise PermissionDenied('You dont have permission to update this profile.')
    #     return obj
    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=user_id)
        return user

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.object.pk})

