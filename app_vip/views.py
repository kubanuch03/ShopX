from rest_framework.viewsets import generics
from .models import Vip
from .serializers import VipCreateSerializer, VipListSerializer

from random import shuffle



class VipListApiView(generics.ListAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipListSerializer

    def get_queryset(self):
        # Получаем изначальный queryset
        queryset = super().get_queryset()
        # Преобразуем его в список
        queryset_list = list(queryset)
        # Перемешиваем список случайным образом
        shuffle(queryset_list)
        # Возвращаем перемешанный queryset
        return queryset_list

class VipDetailApiView(generics.ListAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipListSerializer




class VipCreateApiView(generics.CreateAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer



class VipRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer