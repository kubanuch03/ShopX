from django.shortcuts import render, get_object_or_404
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import WishlistItem
from .serializers import WishlistItemSerializer

from product.models import Product



class WishlistModelViewSet(viewsets.ModelViewSet):
	queryset = WishlistItem.objects.all()
	serializer_class = WishlistItemSerializer
	permission_classes = [IsAuthenticated]
	# permission_classes = [AllowAny,]

	@action(detail=False, methods=["post"])
	def add_wishlist(self, request, *args, **kwargs):
		pid = request.data.get('product')
		product = get_object_or_404(Product, pk=pid)
		if WishlistItem.objects.filter(product=product, user=request.user).exists():
			return Response({'bool': False})
		else:
			WishlistItem.objects.create(product=product, user=request.user)
			return Response({'bool': True})

	@action(detail=False, methods=["get"])
	def my_wishlist(self, request):
		print('---------------------=-=-==-----------------------')
		print(request.user)
		print(WishlistItem.objects.all())
		print('---------------------=-=-==-----------------------')
		queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
		print('---------------------=-=-==-----------------------')
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
'''
 # path('add-wishlist',views.add_wishlist, name='add_wishlist'),
        # path('my-wishlist',views.my_wishlist, name='my_wishlist'),

'''

