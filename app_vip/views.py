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
    queryset = Vip.objects.all()
    serializer_class = VipListSerializer

    def get_queryset(self):
        # Cache key
        cache_key = 'vip_list'
        # Cache timeout
        cache_ttl = getattr(settings, 'CACHE_TTL', 15)

        # Check if the cache exists
        cached_queryset = cache.get(cache_key)
        if cached_queryset:
            return cached_queryset

        # If cache does not exist, fetch from database
        queryset = Vip.objects.all().order_by('-id')
        cache.set(cache_key, queryset, timeout=cache_ttl)
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