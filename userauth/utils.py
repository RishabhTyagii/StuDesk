# utils.py
import random
from django.core.mail import send_mail

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'StudeskPro Email Verification Code'
    message = f'''
Dear User,

Thank you for registering with **StudeskPro**.

To complete your email verification, please use the One-Time Password (OTP) provided below:

🔐 Your OTP: {otp}

This code is valid for the next 10 minutes. Please do not share it with anyone for security reasons.

If you did not request this verification, please disregard this email.

Best regards,  
StudeskPro Support Team  
'''
    from_email = 'rishabtyagi55@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
