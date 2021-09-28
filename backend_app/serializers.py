from rest_framework import serializers
from .models import *
from django.utils import timezone
from .integrations.twilio import *
from .integrations.sendgrid import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'username', 'is_active']#, 'messages', 'recipients']





class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['id', 'first_name', 'last_name', 'user', 'relationship_type', 'email', 'phone', 'is_active']

    def create(self, validated_data):
        request = self.context.get('request')
        recipient = Recipient()
        recipient.first_name = validated_data['first_name']
        recipient.last_name = validated_data['last_name']
        recipient.relationship_type = validated_data['relationship_type']
        recipient.email = validated_data['email']
        recipient.phone = validated_data['phone']
        recipient.user = request.user
        recipient.save()
        return recipient

  



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'user', 'recipient', 'send_date', 'send_sms', 'send_email']

    def create(self, validated_data):
        request = self.context.get('request')
        message = Message()
        message.content= validated_data['content']
        message.recipient = validated_data['recipient']
        message.user = request.user
        message.send_sms = validated_data.get('send_sms', False)
        message.send_email = validated_data.get('send_email', False)
        if message.send_sms:
            to_number = str(validated_data['recipient'].phone)
            client = create_twilio_client()
            send_twilio_sms(client, to_number=to_number, content=validated_data['content'])
        if message.send_email:
            to_email = validated_data['recipient'].email
            send_sendgrid_email(to_email=to_email, content=validated_data['content'])
        message.save()
        return message

