from rest_framework import serializers
from app_chat.models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name','slug',]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['room','user','content','date_added',]