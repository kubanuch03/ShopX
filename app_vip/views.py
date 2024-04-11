from django.shortcuts import render
from rest_framework.viewsets import generics
from .models import Vip
from .serializers import VipCreateSerializer, VipListSerializer





class VipListApiView(generics.ListAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipListSerializer

class VipDetailApiView(generics.ListAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipListSerializer




class VipCreateApiView(generics.CreateAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer



class VipRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vip.objects.all()
    serializer_class = VipCreateSerializer