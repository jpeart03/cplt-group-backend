from .models import *
from .serializers import *
from rest_framework import serializers, viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer





class RecipientViewSet(viewsets.ModelViewSet):
    serializer_class = RecipientSerializer

    def get_queryset(self):
        recps = Recipient.objects.filter(user=self.kwargs['user_pk'])
        return recps

    def perform_create(self, serializer):
        user = AppUser.objects.get(pk=self.kwargs['user_pk'])
        serializer.save(user=user)




class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        mgs = Message.objects.filter(user=self.kwargs['user_pk'])
        return mgs

    def perform_create(self, serializer):
        user = AppUser.objects.get(pk=self.kwargs['user_pk'])

        recipient_pk = self.request.POST['recipient']
        recipient = Recipient.objects.get(pk=recipient_pk)

        serializer.save(user=user, recipient=recipient)

    def perform_destroy(self, instance): # This intentionally prevents deletion of messages
        return

    def perform_update(self, serializer): # This intentionally prevents upding of messages
        return 
        