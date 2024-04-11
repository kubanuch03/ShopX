from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .doc_user import  register_login, forget_password
urlpatterns = [
    path('register/', register_login.user_register_view, name='register'), # регистрация
    path('verify-register-code/', UserVerifyRegisterCode.as_view(), name='verify_register_code'), # подтвердить почту
    path('login/', register_login.user_login_view, name='login'), # логин


    path('refresh-token/', TokenRefreshView.as_view()),
    path('send-code-to-email/', forget_password.user_forget_password_send_view, name='send_password_reset_code'), # отправить code в почту
    path('forget-password/reset/',forget_password.user_forget_password_reset_view, name='reset_password'), # забыл пароль при входе



    
]