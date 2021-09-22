from .models import *
from .serializers import *
from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, date


class SignupView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            AppUser.objects.create_user(email=email, password=password)





class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer





class MessagesList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):        
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





#############################
##### Specialized Views #####
#############################
class UserCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = AppUser.objects.filter(is_active=True).count()
        content = {'user_count': user_count}
        return Response(content)





class MessageCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, start, stop):
        start = datetime.strptime(start, '%Y%m%d').date()
        stop = datetime.strptime(stop, '%Y%m%d').date()
        message_count = Message.objects.filter(send_date__gte=start, send_date__lte=stop).count()
        content = {'message_count': message_count}
        return Response(content)

