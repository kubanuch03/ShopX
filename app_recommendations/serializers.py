from rest_framework import serializers
from app_recommendations.models import Recommendations
from product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]




class RecommendationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ["product"]


class RecommendationListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Recommendations
        fields = ["products"]

    def get_products(self, obj):
        products_queryset = obj.product.all()
        products_data = ProductSerializer(products_queryset, many=True).data
        return products_data