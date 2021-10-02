from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from .models import AppUser 



class AppUserCreationForm(UserCreationForm):    
    class Meta:        
        model = AppUser        
        fields = ('email', )  





class AppUserChangeForm(UserChangeForm):    
    class Meta:        
        model = AppUser        
        fields = UserChangeForm.Meta.fields
