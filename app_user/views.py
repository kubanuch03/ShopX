from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from .services import *
from .serializers import *
from .models import CustomUser as User
from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import logout
from django.core.cache import cache

from drf_spectacular.utils import extend_schema_view, extend_schema

#===================================================================================================================================================================================
class LogoutView(APIView):
    def post(self, request):
        try:
            token = request.headers.get('Authorization').split(' ')[1]
            if cache.get(token):

                
                return Response({"error": "Токен уже недействителен."}, status=status.HTTP_400_BAD_REQUEST)
            cache.set(token, True, timeout=None)  # Устанавливаем токен в кэш без срока действия
            return Response({"message": "Вы успешно вышли из системы."}, status=status.HTTP_200_OK)
        except AttributeError:
            return Response({"error": "Отсутствует заголовок Authorization."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

#отправить код на почту       
class ForgetPasswordSendCodeView(generics.UpdateAPIView):
    serializer_class = SendCodeSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        email_or_phone = request.data.get("email_or_phone")
        if not email_or_phone:
            return Response({"required": "email_or_phone"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email_or_phone=email_or_phone)
            # Если пользователь уже существует, просто обновите его код подтверждения и отправьте его
            send_verification_code(email_or_phone=email_or_phone)
            return Response({"success":"Код был отправлен на почту/телефон"}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            # Если пользователь не существует, создайте нового пользователя и отправьте ему код подтверждения
            user = CustomUser.objects.create(email_or_phone=email_or_phone)
            send_verification_code(email_or_phone=email_or_phone)
            return Response({"success":"Код был отправлен на почту/телефон"}, status=status.HTTP_201_CREATED)


# если user забыл пароль при входе
class ForgetPasswordView(generics.UpdateAPIView):
    serializer_class = ForgetPasswordSerializer

    http_method_names = ['patch',]
    def update(self, request, *args, **kwargs):
        
        result = ChangePasswordOnReset.change_password_on_reset(self=self,request=request)

        if result == "success":
            return Response({"success ":"Пароль успешно изменен"}, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)



# ==== User =============================================================================================================================================================

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_superuser=False)
    # serializer_class = UserRegisterSerializer
    serializer_class = UserListSerializer

# апи для регистрации
class UserRegisterView(CreateUserApiView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

# апи для логина
class UserLoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email_or_phone = request.data.get('email_or_phone')
        password = request.data.get('password')

        if not email_or_phone or not password:
            return Response({'error':'Both email/phone and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(email_or_phone=email_or_phone)
        except CustomUser.DoesNotExist:
            return Response({'error':'The user does not exist'})
        if not check_password(password, user.password):
            return Response({'error':'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        refresh = RefreshToken.for_user(user=user)
        access_token = refresh.access_token
        return Response({
            'detail': 'Successfully confirmed your code',
            'id': user.id,
            'is_seller': user.is_usual,
            'email': user.email_or_phone,
            'refresh': str(refresh),
            'access': str(access_token),
            'refresh_lifetime_days': refresh.lifetime.days,
            'access_lifetime_seconds': access_token.lifetime.total_seconds()
        })


# апи который проверяет код который был отправлен на указанный email и в ответ передает токен
class UserVerifyRegisterCode(generics.UpdateAPIView):
    serializer_class = VerifyCodeSerializer

    http_method_names = ['patch',]
    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        

        return CheckCode.check_code(code=code,)
    

class UserProfile():
    pass





