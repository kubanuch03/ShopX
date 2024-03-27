from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from .services import *
from .serializers import *
from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema



#===================================================================================================================================================================================
class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        user = request.user
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                user.device_token = None
                user.save()
                return Response({'message': 'Вы успешно вышли из системы.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Недопустимый токен.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Токен не предоставлен.'}, status=status.HTTP_400_BAD_REQUEST)
        

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


class MarketListAPIView(generics.ListAPIView):
    queryset = SellerProfile.objects.prefetch_related('products').all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10


# ==== User =============================================================================================================================================================

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
        try:
            user = CustomUser.objects.get(email_or_phone=email_or_phone)
        except CustomUser.DoesNotExist:
            return Response({'error':'The user does not exist'})
        
        refresh = RefreshToken.for_user(user=user)
        access_token = refresh.access_token
        return Response({
            'detail': 'Successfully confirmed your code',
            'id': user.id,
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
        return CheckCode.check_code(code=code)
    

# ===== Продавец Seller ====================================================================================================================================================================

class SellerListApiview(generics.ListAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticated,]


class SellerUpdateProfileApi(generics.UpdateAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    http_method_names = ['patch',]
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field = 'id'


class SellerDetailProfileApi(generics.RetrieveAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    lookup_field = 'id'


class SellerRegisterView(CreateUserApiView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerRegisterSerializer
     


# апи для того чтобы сттать продавцом 
class BecomeSellerView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BecomeSellerSerializer
    
    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        user = CustomUser.objects.get(id=user_id)
        username = user.username
        email_or_phone = user.email_or_phone
        password = user.password
        is_active = user.is_active
        number = user.number
        user.delete()
        new_seller = SellerProfile.objects.create(
            username=username,
            email_or_phone=email_or_phone,
            password=password,
            is_active=is_active,
            number = number,
            is_seller = True)
        
        new_seller.save()
        return Response({'success':f"Вы успешно стали продавцом{new_seller}"}, status=status.HTTP_200_OK)












# === Profile =========================================================================================================================================================
    
# апи менят пароль в профиле 
class UserResetPasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['patch',]
    def update(self, request, *args, **kwargs):
            result = ChangePassword.change_password_on_profile(request=request)

            if result == "success":
                return Response({"success":"Пароль успешно изменен"}, status=status.HTTP_200_OK)
            else:
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

class ListProfileApi(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer



class UpdateUserProfileApi(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['patch',]
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field = 'id'

class DetailUserProfileApi(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'


#==============================================================================================================================================================================







