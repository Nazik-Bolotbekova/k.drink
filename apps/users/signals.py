# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from apps.users.models import CustomUser
# from core import settings
#
# @receiver(post_save, sender=CustomUser)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Welcome to our website'
#         message = f'Hi {instance.username} thank you for registering'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [instance.email]
#         send_mail(subject,message,email_from,recipient_list)
#