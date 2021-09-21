from rest_framework import serializers
from .models import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'username', 'password']#, 'messages', 'recipients']





class RecipientSerializer(serializers.ModelSerializer):
    # user = AppUserSerializer(many=True, read_only=True)
    # relationship_type = serializers.StringRelatedField(read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Recipient
        fields = ['id', 'first_name', 'last_name', 'user', 'relationship_type', 'email', 'phone']

    def create(self, validated_data):
        print('createSerializer')
        print(validated_data)
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

    def get_user(self, obj):
        return obj.user.id



class MessageSerializer(serializers.ModelSerializer):
    # user = AppUserSerializer(many=True, read_only=True)
    # recipient = RecipientSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'content', 'user', 'recipient', 'send_date']

    def create(self, validated_data):
        print('createSerializer')
        request = self.context.get('request')
        # print(validated_data['recipient'])
        # rec = Recipient.objects.get(id=validated_data['recipient'])
        message = Message()
        message.content= validated_data['content']
        message.recipient = validated_data['recipient']
        message.user = request.user
        message.save()
        return message

    def get_user(self, obj):
        return obj.user.id

