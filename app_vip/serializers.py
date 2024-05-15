from rest_framework import serializers
from .models import Vip
from product.models import Product
from product. serializers import ProductSerializer





class VipCreateSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(required=True)

    class Meta:
        model = Vip
        fields = ['id',"product",'icon']
    
    # def create(self, validated_data):
    #     product_id = validated_data['product']
    #     if Vip.objects.filter(product=product_id).exists():
    #         raise serializers.ValidationError({"dublicate":"уже существует"})
    #     return super().create(validated_data)
        


class VipListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Vip
        fields = ['id',"products",'icon']
        

    def get_products(self, obj):
        products_queryset = obj.product.all()
        products_data = ProductSerializer(products_queryset, many=True).data
        return products_data
    