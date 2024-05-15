from rest_framework.viewsets import generics
from rest_framework import response
from django.db import transaction
from django.db.models.functions import Random
from django.core.cache import cache
from django.conf import settings
from .models import Vip
from .serializers import VipCreateSerializer, VipListSerializer

from random import shuffle



class VipListApiView(generics.ListAPIView):
    serializer_class = VipListSerializer

    def get_queryset(self):
        cache_key = 'vip_list'
        cache_ttl = getattr(settings, 'CACHE_TTL', 15)

        cached_queryset = cache.get(cache_key)
        

        if cached_queryset is not None:  
            print('Кеш найден!')
            return cached_queryset

        queryset = list(Vip.objects.all().order_by('-id'))  
        cache.set(cache_key, queryset, timeout=cache_ttl)
        print('кеш не найден')
        return queryset


class VipDetailApiView(generics.ListAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipListSerializer




class VipCreateApiView(generics.CreateAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product') 
        
        
        if Vip.objects.select_related('product').filter(product__id=product_id).exists():
            return response.Response({"error": "this product already exists"})
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({"success": f"Vip created successfully"})
    
    def perform_create(self, serializer):
        serializer.save()



class VipRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer