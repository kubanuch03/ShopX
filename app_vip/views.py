from rest_framework.viewsets import generics
from rest_framework import response
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

    def create(self, request, *args, **kwargs):
        vip_id = request.data.get('id')  # Получаем идентификатор из запроса
        product_id = request.data.get('product') 
        
        vip_exists = Vip.objects.filter(product__id=product_id).exists()
        if vip_exists:
            return response.Response({"error": "this product already exists"})
        
        vip_serializer = self.get_serializer(data=request.data)
        vip_serializer.is_valid(raise_exception=True)
        vip_serializer.save()
        return response.Response({"success": f"Vip created successfully"})
        



class VipRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer