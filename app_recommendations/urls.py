from django.contrib import admin
from django.urls import path
from app_recommendations.views import RecommendationCreateApiView, RecommendationListApiView, RecommendationRUDApiView


urlpatterns = [
    path('list/recommendation/', RecommendationListApiView.as_view()),
    path('create/recommendation/', RecommendationCreateApiView.as_view()),
    path('rud/recommendation/<int:id>/', RecommendationRUDApiView.as_view()),
]


