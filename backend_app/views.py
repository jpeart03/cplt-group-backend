from .models import *
from .serializers import *
from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import AllowAny


class SignupView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            print(serializer.validated_data)
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            AppUser.objects.create_user(email=email, password=password)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class MessagesList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):        
        print('createview')
        serializer.save()

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(user=user)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(user=user)

    def perform_destroy(self, instance): # This intentionally prevents deletion of messages
        return

    def perform_update(self, serializer): # This intentionally prevents upding of messages
        return 

class RecipientList(generics.ListCreateAPIView):
    serializer_class = RecipientSerializer

    def perform_create(self, serializer):
        user = self.request.user.id    
        print('createview')
        print('user', user)
        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        return Recipient.objects.filter(user=user)


class RecipientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipientSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        user = self.request.user
        return Recipient.objects.filter(user=user)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = AppUser.objects.all()
#     serializer_class = AppUserSerializer





# class RecipientViewSet(viewsets.ModelViewSet):
#     serializer_class = RecipientSerializer

#     def get_queryset(self):
#         recps = Recipient.objects.filter(user=self.kwargs['user_pk'])
#         return recps

#     def perform_create(self, serializer):
#         user = AppUser.objects.get(pk=self.kwargs['user_pk'])
#         serializer.save(user=user)




# class MessageViewSet(viewsets.ModelViewSet):
#     serializer_class = MessageSerializer

#     def get_queryset(self):
#         mgs = Message.objects.filter(user=self.kwargs['user_pk'])
#         return mgs

#     def perform_create(self, serializer):
#         user = AppUser.objects.get(pk=self.kwargs['user_pk'])

#         recipient_pk = self.request.POST['recipient']
#         recipient = Recipient.objects.get(pk=recipient_pk)

#         serializer.save(user=user, recipient=recipient)

#     def perform_destroy(self, instance): # This intentionally prevents deletion of messages
#         return

#     def perform_update(self, serializer): # This intentionally prevents upding of messages
#         return 
        