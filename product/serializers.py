from rest_framework import serializers
from .models import Product, Recall, RecallImages, Size
from app_user.serializers import UserProfileSerializer, UserRecallSerializer

class ProductSerializer(serializers.ModelSerializer):
    location = serializers.CharField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    likes = serializers.IntegerField(read_only=True)
    discount = serializers.IntegerField(required=False)
    mid_ocenka = serializers.SerializerMethodField() 
    count_recall = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def apply_discount_to_price(self, price, discount):
        if discount > 0 and discount <= 100:
            discounted_price = price - (price * discount) // 100
            return discounted_price
        else:
            return price

    def create(self, validated_data):
        price = validated_data['price']
        discount = validated_data['discount']
        if price <= 0 or discount <=0:
            raise serializers.ValidationError({"price or discount": "Price or Discount must be a positive integer."})

        if discount is not None:
            discounted_price = self.apply_discount_to_price(price, discount)
            validated_data['discounted_price'] = discounted_price
        return super().create(validated_data)



    def get_mid_ocenka(self, instance):
        # Вычисляем среднюю оценку товара
        recalls = instance.recall_set.all()
        if recalls.exists():
            total_rating = sum(recall.rating for recall in recalls)
            mid_ocenka = total_rating / recalls.count()
            return mid_ocenka
        else:
            return None

    def get_count_recall(self,instance):
        recalls = instance.recall_set.all()
        count_recall = recalls.count()
        return count_recall

    



class RecallSerializer(serializers.ModelSerializer):
    user= UserRecallSerializer(read_only=True)
    class Meta:
        model = Recall
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True, }, 'created': {'read_only': True, },
                        'updated': {'read_only': True, },
                        }

    def to_representation(self, instance):
        data_recall = super().to_representation(instance) 
        data_recall['user'] = UserRecallSerializer(instance.user.all(), many=True, context=self.context).data

        return data_recall


class RecallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecallImages
        fields = ['id','images']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'sizes']