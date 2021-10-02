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

    worlds_best_boss_1 = models.BooleanField(default=False)
    worlds_best_boss_2 = models.BooleanField(default=False)
    worlds_best_boss_3 = models.BooleanField(default=False)
    cassanova_1 = models.BooleanField(default=False)
    cassanova_2 = models.BooleanField(default=False)
    cassanova_3 = models.BooleanField(default=False)
    short_and_sweet = models.BooleanField(default=False)
    dickens = models.BooleanField(default=False)
    it_takes_committment_1 = models.BooleanField(default=False)
    it_takes_committment_2 = models.BooleanField(default=False)
    it_takes_committment_3 = models.BooleanField(default=False)
    sleep_mode = models.BooleanField(default=False)
    lunch_break = models.BooleanField(default=False)
    forget_me_not = models.BooleanField(default=False)
    networking_1 = models.BooleanField(default=False)
    networking_2 = models.BooleanField(default=False)
    networking_3 = models.BooleanField(default=False)
    sentimental = models.BooleanField(default=False)
    # send_i_mental = models.BooleanField(default=False)
    what_year_is_it = models.BooleanField(default=False)
    nerd = models.BooleanField(default=False)
    old_school = models.BooleanField(default=False)

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


