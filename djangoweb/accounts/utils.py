from django.contrib.auth import get_user_model

UserModel = get_user_model()


def get_user_by_username(username):
    return UserModel.objects.filter(user__username=username).get()
