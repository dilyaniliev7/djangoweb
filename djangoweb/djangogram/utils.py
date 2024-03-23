from django.contrib.auth import get_user_model
from django.shortcuts import redirect


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


# class OwnerRequiredMixin:
#     model = get_user_model()
#
#     def get_object(self, queryset=None):
#         obj = self.get_object()
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#
#         if request.user == self.object.user:
#             return super().get(request, *args, **kwargs)
#         else:
#             return redirect('index.html')
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#
#         if request.user == self.object.user:
#             return super().post(request, *args, **kwargs)
#         else:
#             return redirect('index.html')
