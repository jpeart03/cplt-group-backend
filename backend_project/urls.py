from backend_app.views import UserCountView
from django.contrib import admin
from django.urls import path, include, re_path
from backend_app.views import UserCountView, MessageCountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('backend_app.urls')),
    path('user_count/', UserCountView.as_view()),
    path('message_count/', MessageCountView.as_view()),
]
