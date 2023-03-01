from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_verification_otp(email,otp):
    subject = 'Your OTP'
    message = f'your OTP number is - {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True