from rest_framework import serializers
from .models import Category, PodCategory

class PodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PodCategory
        fields = ("id", "name", "category", "slug")
        read_only_fields = ("id", "slug")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "img", "pod_categories")
        read_only_fields = ("id", "slug") 
