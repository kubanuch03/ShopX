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
	# permission_classes = [IsAuthenticated,]
	permission_classes = [AllowAny,]

	@action(detail=False, methods=["post"])
	def add_wishlist(self, request, *args, **kwargs):
		print(request.data, '>>>>>>> product in wishlist add ')
		# pid = request.data.get('product')
		pid = request.data.get('id', None)
		product = get_object_or_404(Product, pk=pid)
		if WishlistItem.objects.filter(product=product, user=request.user).exists():
			return Response({'bool': False})
		else:
			WishlistItem.objects.create(product=product, user=request.user)
			return Response({'bool': True})

	# @action(detail=False, methods=["get"])
	# def my_wishlist(self, request):
	# 	# if request.user.is_authenticated:
	# 	# 	queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
	# 	# 	serializer = self.get_serializer(queryset, many=True)
	# 	# 	return Response(serializer.data)
	# 	# else:
	# 	# 	return Response(
	# 	# 		{"detail": "User is not authenticated"},
	# 	# 		status=status.HTTP_401_UNAUTHORIZED
	# 	# 	)
	# 	queryset = WishlistItem.objects.all()
	# 	serializer = WishlistItemSerializer(queryset, many=True)
	# 	return Response(serializer.data)

	@action(detail=False, methods=["get"])
	def my_wishlist(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response(
				{"detail": "User is not authenticated"},
				status=status.HTTP_401_UNAUTHORIZED
			)




	@action(detail=False, methods=["get"])
	def my_wishlist(self, request, *args, **kwargs):
		email_or_phone = request.data.get('email_or_phone')
		# email_or_phone = request.query_params.get('email_or_phone', None)

		# print(password, '>>>>>>> password in my_wishlist')

		print(email_or_phone, 'email or phone -=-=-=-=-=-=-=-=-')
		print(args, ' args kwargs ', kwargs)

		print('---------------------=-=-==-----------------------')
		# print(request.user)
		# print(WishlistItem.objects.all())
		print('---------------------=-=-==-----------------------')
		# print(email_or_phone)
		# print(password)
		# print(request.GET)
		print(self.request, '--------1')
		print('---------------------=-=-==-----------------------')


		if request.user.is_authenticated:
			queryset = WishlistItem.objects.filter(user=request.user).order_by('-id')
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response(
				{"detail": "User is not authenticated"},
				status=status.HTTP_401_UNAUTHORIZED
			)

'''
	
	GET /wishlist/my-wishlist/?email_or_phone=email@example.com&password=examplepassword
	
	
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
'''

@action(detail=False, methods=["post"])
 		path('add-wishlist',views.add_wishlist, name='add_wishlist'),
        path('my-wishlist',views.my_wishlist, name='my_wishlist'),

{
    "email_or_phone": "mirbekov1kylych@gmail.com",
    "password": "qwerty1993"
}


'''

