from rest_framework import serializers
from .models import Category, PodCategory




class PodCategorySerializer(serializers.ModelSerializer):
    Category = Category()

    class Meta:
        model = PodCategory
        fields = ("id", "name", "category", "slug")
        read_only_fields = ("id", "slug")

class CategorySerializer(serializers.ModelSerializer):
    pod_categories = PodCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "img", "pod_categories")
        read_only_fields = ("id", "slug")