from backend_app.models import AppUser, Message, Recipient
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import AppUserChangeForm, AppUserCreationForm


# Register your models here.

admin.site.register(Recipient)
admin.site.register(Message)

class AppUserAdmin(UserAdmin):    
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ['username']

admin.site.register(AppUser, AppUserAdmin)