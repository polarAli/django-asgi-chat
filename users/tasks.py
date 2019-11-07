import logging

from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from workshop.celery import app
from users.tokens import account_activation_token


@app.task
def send_email(mail_subject, message, to):
    email = EmailMessage(
        mail_subject, message, to=to)
    email.send(fail_silently=False)


@app.task
def send_confirmation_mail(user_id, current_domain):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        mail_subject = 'Activate your account.'
        message = render_to_string('users/account_active_email.html', {
            'user': user,
            'domain': current_domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_email.delay(mail_subject, message, to=[user.email])
    except UserModel.DoesNotExist:
        logging.warning(f"Tried to send verification email to non-existing user {user_id}")
    except KeyError as e:
        print(e)
