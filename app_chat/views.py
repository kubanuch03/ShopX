from rest_framework import generics, permissions, status
from rest_framework.response import Response

from app_chat.models import Room
from app_chat.serializers import RoomSerializer, MessageSerializer

from app_chat.models import Room, Message

class RoomRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        # Получить все комнаты, в которых текущий пользователь является создателем
        created_rooms = Room.objects.filter(users=user)
        # Получить все комнаты, в которых текущий пользователь участвует
        joined_rooms = Room.objects.filter(users=user)
        # Объединить списки созданных и присоединенных комнат
        queryset = created_rooms | joined_rooms
        return queryset.distinct()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        room = self.get_object()
        messages = Message.objects.filter(room=room)[:25]
        serializer = self.get_serializer(room)
        data = serializer.data
        data['messages'] = MessageSerializer(messages, many=True).data
        return Response(data)



class RoomCreateAPIView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]



class RoomDeleteAPIView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(users=user)

    



class RoomListAPIView(generics.ListAPIView):
    # queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Получить все комнаты, в которых текущий пользователь является создателем
        created_rooms = Room.objects.filter(users=user)
        # Получить все комнаты, в которых текущий пользователь участвует
        joined_rooms = user.rooms.all()
        # Объединить списки созданных и присоединенных комнат и убрать дубликаты
        queryset = created_rooms.union(joined_rooms)
        return queryset