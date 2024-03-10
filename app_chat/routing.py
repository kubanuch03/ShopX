from django.urls import path

from app_chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<str:room_name>/', ChatConsumer.as_asgi()),
]



