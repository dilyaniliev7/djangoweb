from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_sign_up(instance, created, **kwargs):
    if not created:
        return

    send_mail(
        subject='Welcome to Socialgram!',
        message='You just signed up!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(instance.email,),
    )
