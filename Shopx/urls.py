from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .yasg import urlpatterns as doc


# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularRedocView,
#     SpectacularSwaggerView,
# )




urlpatterns = [
    path("admin/", admin.site.urls),
    path("chats/", include("app_chat.urls")),
    path("support/", include("app_support_service.urls")),
    path("category/", include("Category.urls")),
    path("products/", include("product.urls")),
    path('user/', include("app_user.urls")),
    path('seller/', include("app_userseller.urls")),
    path('baner/', include("app_baner.urls")),
    path('vip/', include("app_vip.urls")),
    path('wishlist/', include("app_wishlist.urls")),
]
urlpatterns+=doc

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

