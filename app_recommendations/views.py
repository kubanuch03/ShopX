from django.shortcuts import render
from rest_framework.viewsets import generics
from app_recommendations.models import Recommendations
from app_recommendations.serializers import RecommendationCreateSerializer, RecommendationListSerializer





class RecommendationListApiView(generics.ListAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationListSerializer


class RecommendationCreateApiView(generics.CreateAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationCreateSerializer



class RecommendationRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationCreateSerializer
    lookup_field = "id"