from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import django.dispatch

from django_rest_resetpassword.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
import logging

from .models import Users

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler and set its level and formatter
# log_file = logging.FileHandler("logfile.log")
# log_file.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# log_file.setFormatter(formatter)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:

        subject = 'Welcome to Farmers App'
        message = 'We are glad to have you on board. We hope you enjoy our services.'
        send_mail(
            subject,    
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )

# @receiver(post_save, sender=User)
# def save_profile(sender, instance,created, **kwargs):
#     instance.user.save()



# __all__ = [
#     'reset_password_token_created',
#     'pre_password_reset',
#     'post_password_reset',
# ]

# reset_password_token_created = django.dispatch.Signal()

# pre_password_reset = django.dispatch.Signal()

# post_password_reset = django.dispatch.Signal()



# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender: View Class that sent the signal
#     :param instance: View Instance that sent the signal
#     :param reset_password_token: Token Model Object
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#         'current_user': reset_password_token.user,
#         'username': reset_password_token.user.username,
#         'email': reset_password_token.user.email,
#         'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
#     }

#     # render email text
#     email_html_message = render_to_string('email/user_reset_password.html', context)
#     email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

#     msg = EmailMultiAlternatives(
#         # title:
#         "Password Reset for {title}".format(title="Some website title"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()
