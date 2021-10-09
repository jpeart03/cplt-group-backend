from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework_nested import routers
from django.conf.urls import url

urlpatterns = [
    path('auth/', include('rest_auth.urls')),    
    path('auth/register/', include('rest_auth.registration.urls')),
    path('recipients/', RecipientList.as_view()),
    path('recipients/<int:id>/', RecipientDetail.as_view()),
    path('messages/', MessagesList.as_view()),
    path('messages/<int:id>/', MessageDetail.as_view()),
    path('message_count/', MessageCountView.as_view()),
]