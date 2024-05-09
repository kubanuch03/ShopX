from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# from .doc_user_profile import  register_login, forget_password
urlpatterns = [
#     path('register/', register_login.user_register_view, name='register'), # регистрация
    path('verify-register-code/', SellerVerifyRegisterCode.as_view(), name='seller-verify_register_code'), # подтвердить почту
    path('login/', SellerLoginView.as_view(), name='seller-login'), # логин


#     path('refresh-token/', TokenRefreshView.as_view()),
    path('send-code-to-email/', SellerForgetPasswordSendCodeView.as_view(), name='send_password_reset_code'), # отправить code в почту
#     path('forget-password/reset/',forget_password.user_forget_password_reset_view, name='reset_password'), # забыл пароль при входе


#     path('profiles/', ListProfileApi.as_view(), name=''),
#     path('profile/<int:id>/', DetailUserProfileApi.as_view(), name=''),
#     path('profile/update/<int:id>/', UpdateUserProfileApi.as_view(), name=''),
#     path('reset-password-profile/', UserResetPasswordView.as_view(), name='reset_password'),


    path('seller/register/',SellerRegisterView.as_view(), name='seller-register'),
#     path('seller/login/',SellerLoginView.as_view(), name='seller-login'),
    path('become/seller/', BecomeSellerView.as_view(), name='seller-become_seller'),
    path('seller/profiles/detail/<int:pk>/',SellerDetailApiview.as_view(),name='seller-profile-detail'),
    path('seller-profiles/',SellerListApiview.as_view()),
#     path('seller-profile/<int:id>/', DetailUserProfileApi.as_view(), name=''),
    path('seller/profile/update/<int:pk>/', SellerUpdateProfileShopApi.as_view(), name='seller-profile-update'),

    path('logout/seller/', LogoutView.as_view(), name='user logout'),

    path('change/password/seller/', ChangePasswordAPIVIew.as_view()),

#     path('market/', MarketListAPIView.as_view(), name=''),
#     path('logout/', LogoutView.as_view(), name='logout'),
    
]