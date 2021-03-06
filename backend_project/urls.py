from backend_app.views import UserCountView
from django.contrib import admin
from django.urls import path, include, re_path
from backend_app.views import UserCountView, MessageCountView, MessageCountByDayView, WordCountView, GeneratePromptView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('backend_app.urls')),
    path('user_count/', UserCountView.as_view()),
    path('word_count/', WordCountView.as_view()),
    path('generate_prompt/', GeneratePromptView.as_view()),
    path('message_count_by_day/', MessageCountByDayView.as_view()),
]
