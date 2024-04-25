from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import WishlistModelViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        # path("users/entry-check/", WishlistItemViewSet.as_view({"get": "list"}), name="entry-chick-list"),
        #
        # # Wishlist
        path('add-wishlist/', WishlistModelViewSet.as_view({"post": "add_wishlist"}), name='add_wishlist'),
        path('my-wishlist/', WishlistModelViewSet.as_view({"get": "my_wishlist"}), name='my_wishlist'),
        path('test_/', WishlistModelViewSet.as_view({'get': 'test_method'}), name='test_wishlist'),
    ]
)