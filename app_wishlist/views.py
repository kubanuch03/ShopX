from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import WishlistItem
from .serializers import WishlistItemSerializer
from product.models import Product



class WishlistModelViewSet(viewsets.ModelViewSet):
	queryset = WishlistItem.objects.all()
	serializer_class = WishlistItemSerializer
	permission_classes = [IsAuthenticated]

	@action(detail=False, methods=["get"])
	def test_method(self, request, *args, **kwargs):

		return Response(
			{
				'message': 'This is a test method. It works!',
				'user_id': request.user.id,
			}
		)

	@action(detail=False, methods=["post"])
	def add_wishlist(self, request, *args, **kwargs):
		print(request.data, '>>>>>>> product in wishlist add ')
		# pid = request.data.get('product')
		pid = request.data.get('id', None)
		product = get_object_or_404(Product, pk=pid)
		if WishlistItem.objects.filter(product=product, user=request.user).exists():
			return Response(
				{
					'message': 'Product already exists in wishlist',
					'success': False
				},
					status=status.HTTP_400_BAD_REQUEST)
		else:
			WishlistItem.objects.create(product=product, user=request.user)
			return Response(
				{
					'message': 'Product added to wishlist',
					'success': True
				},
				status=status.HTTP_201_CREATED)

	@action(detail=False, methods=["get"])
	def my_wishlist(self, request):
		if request.user.is_authenticated:
			queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response(
				{"detail": "User is not authenticated"},
				status=status.HTTP_401_UNAUTHORIZED
			)

	@action(detail=False, methods=["post"])
	def remove_wishlist(self, request, *args, **kwargs):
		product_id = request.data.get('product', None)
		product = Product.objects.get(pk=product_id)
		wishlist_item = WishlistItem.objects.filter(product=product).first()

		if wishlist_item:
			wishlist_item.delete()
			return Response(
				{
					'message': 'Product removed from wishlist',
					'success': True
				},
				status=status.HTTP_200_OK
			)
		else:
			return Response(
				{
					'message': 'Product does not exist in wishlist',
					'success': False
				},
				status=status.HTTP_400_BAD_REQUEST
			)



