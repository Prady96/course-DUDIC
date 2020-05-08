from django.conf import settings
from django.core.mail import send_mail

def mail_after_registeration(name, ):
    subject = 'Thank for registeration'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = 'DUDIC Portal'
    recipient_list = ['pradyumg@gmail.com',]
    


send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)