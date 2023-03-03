from celery import shared_task
from django.core.mail import send_mail
from blog import settings


@shared_task(bind=True)
def send_mail_func(*args, **kwargs):
    send_mail(
        'Blog Created',
        f"Your blog has been created successfully.",
        settings.EMAIL_HOST_USER,
        [kwargs["email_id"]],
        fail_silently=False,
    )
    return True

