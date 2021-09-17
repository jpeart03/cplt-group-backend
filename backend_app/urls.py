from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework_nested import routers
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

users_router = routers.NestedSimpleRouter(router, r'', lookup='users')
users_router.register(r'messages', MessageViewSet, basename='users-messages')


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(users_router.urls)),
]