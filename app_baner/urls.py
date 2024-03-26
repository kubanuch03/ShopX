from django.urls import path

from .views import (
    BanerCreateListView,
    BanerDeleteView,
    BanerDetailView,
    BanerListView,
    BanerUpdateView
)


urlpatterns = [
    path("list/baner/",BanerListView.as_view(),name='list-baner'),
    path("detail/baner/<int:pk>/",BanerDetailView.as_view(),name='detail-baner'),

    path("create/baner/",BanerCreateListView.as_view(),name='create-list-baner'),
    path("update/baner/<int:pk>/",BanerUpdateView.as_view(),name='update-baner'),
    path("delete/baner/<int:pk>/",BanerDeleteView.as_view(),name='delete-baner'),



]