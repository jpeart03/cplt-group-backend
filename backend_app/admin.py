from backend_app.models import AppUser, Message, Recipient
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Recipient)
admin.site.register(Message)