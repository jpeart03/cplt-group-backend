from rest_framework import serializers
from .models import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']





class RecipientSerializer(serializers.ModelSerializer):
    user = AppUserSerializer(many=True, read_only=True)
    relationship_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Recipient
        fields = ['id', 'first_name', 'last_name', 'user', 'relationship_type', 'email', 'phone']





class MessageSerializer(serializers.ModelSerializer):
    sender = AppUserSerializer(many=True, read_only=True)
    recipieint = RecipientSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'content', 'sender', 'recipient']