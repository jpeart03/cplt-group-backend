from .models import *
from .serializers import *
from rest_framework import serializers, viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer





class RecipientViewSet(viewsets.ModelViewSet):
    serializer_class = RecipientSerializer

    def get_queryset(self):
        return Recipient.objects.filter(user=self.kwargs['users_pk'])

    def perform_create(self, serializer):
        user = AppUser.object.get(pk=self.kwargs['users_pk'])
        serializer.save(user=user)




class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(user=self.kwargs['users_pk'])

    def perform_create(self, serializer):
        user = AppUser.objects.get(pk=self.kwargs['users_pk'])
        recipient = Recipient.objects.get(pk=self.kwargs['recipients_pk'])
        serializer.save(user=user, recipient=recipient)