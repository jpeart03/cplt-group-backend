from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class AppUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField() # Retreive using User.phone.as_e164 for Twillio
    is_active = models.BooleanField(default=True)


    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





class Recipient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="recipients")
    relationship_type = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





class Message(models.Model):

    content = models.TextField()
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="messages")
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, related_name="messages")
    send_date = models.DateTimeField(default=timezone.now)
    send_sms = models.BooleanField(default=False)
    send_email = models.BooleanField(default=False)
    sent_to_email = models.CharField(max_length=100, default='')
    sent_to_phone = PhoneNumberField(default='')

    def __str__(self):
        return f"From: {self.user.first_name} {self.user.last_name}.  To: {self.recipient.first_name} {self.recipient.last_name}"


