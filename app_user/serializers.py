from rest_framework import serializers
from .models import CustomUser
from product.serializers import Product
from Category.serializers import CategorySerializer, PodCategorySerializer

class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    username = serializers.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ['email_or_phone','username','password','password_confirm']


    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs
    

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        return user
        
    


class VerifyCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['code']


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    email_or_phone = serializers.CharField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ['email_or_phone','password']
    
    def validate(self, attrs):
        email_or_phone = attrs.get('email_or_phone')
        password = attrs.get('password')

        if not email_or_phone or not password:
            raise serializers.ValidationError("Both email/phone and password are required")

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)
    
    class Meta:
        fields = ['old_password',
                  'new_password',
                  'confirm_new_password',]

class SendCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email_or_phone']


class ForgetPasswordSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6,write_only=True)
    password = serializers.CharField(max_length=20,write_only=True)
    confirm_password = serializers.CharField(max_length=20,write_only=True)

    class Meta:
        fields = ['password','confirm_password','code']



class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username',
                  'surname',
                  'email_or_phone',
                  'number',
                  'gender',
                  ]
  
class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    class Meta:
        fields = ['refresh_token',]