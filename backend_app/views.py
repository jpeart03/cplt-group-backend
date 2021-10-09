from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, date
from django.utils.timezone import make_aware
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re
from .prompts.generate_prompt import generate_prompt


class SignupView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            AppUser.objects.create_user(email=email, password=password)





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
        return Recipient.objects.filter(user=user, is_active=True)





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

    def get(self, request):
        user_count = AppUser.objects.filter(is_active=True).count()
        content = {'user_count': user_count}
        return Response(content)





class MessageCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        start = self.request.query_params.get('start')
        stop = self.request.query_params.get('stop')

        if start:
            start = make_aware(datetime.strptime(start, '%Y%m%d'))
        else:
            start = make_aware(datetime.strptime('20210830', '%Y%m%d'))

        if stop:
            stop = make_aware(datetime.strptime(stop, '%Y%m%d'))
        else:
            stop = timezone.now()

        messages = Message.objects.filter(send_date__gte=start, send_date__lte=stop)
        dates = [message.send_date.date().strftime("%Y-%m-%d") for message in messages]
    
        message_count = Counter(dates)
        content = []
        for k, v in message_count.items():
            content.append({'name': k, 'value': v})
        return Response(content)





class MessageCountByDayView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        messages = Message.objects.all()
        days = [message.send_date.date().weekday() for message in messages]
        content = Counter(days)
        return Response(content)





class WordCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        messages = Message.objects.all() # Get the message queryset
        contents_list = [message.content for message in messages] # Extract the objects' content
        contents_str = ' '.join(contents_list) # Join into a single string
        contents_no_punc = re.sub(r'[^\w\s]', '', contents_str) # Remove punctuation
        contents_tokens = word_tokenize(contents_no_punc.lower()) # Tokenize and lower case
        filtered_tokens = [word for word in contents_tokens if not word in stopwords.words()] # Count the values
        content = []
        word_count = Counter(filtered_tokens)
        
        for k, v in word_count.items():
            content.append({'value': k, 'count': v})

        return Response(content)


class GeneratePromptView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        content = {'prompt': generate_prompt(request.data['relationship_type'])}
        return Response(content)