from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# class AppUser(AbstractUser):
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField() # Retreive using User.phone.as_e164 for Twillio

    # username = models.CharField(max_length=100, default="username")
    # password = models.CharField(max_length=100, default="pw123")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Recipient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="recipients")
    relationship_type = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="messages")
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return f"From: {self.sender.first_name} {self.sender.last_name}.  To: {self.recipient.first_name} {self.recipient.last_name}"


