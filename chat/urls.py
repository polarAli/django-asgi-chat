from django.urls import path
from .views import index, chat

urlpatterns = [
    path('', index, name='chat-index'),
    path('chat/<str:room_name>/', chat, name='chat-room')
]
