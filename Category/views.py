from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Category, PodCategory
from .serializers import CategorySerializer, PodCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics, response, status


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Дополнительная проверка на существование объекта с такими же данными
        name = serializer.validated_data.get('name')
        if Category.objects.filter(name=name).exists():
            return response.Response({'error': 'Категория с таким именем уже существует'}, status=400)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=201, headers=headers)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        AllowAny,
    ]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        query = self.request.query_params.get("search", "")
        return Category.objects.filter(name__icontains=query)



class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        AllowAny,
    ]


class PodCategoryViewSet(ModelViewSet):
    queryset = PodCategory.objects.all()
    serializer_class = PodCategorySerializer
    permission_classes = [
        AllowAny,
    ]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name", "category"]
    def get_queryset(self):
        query = self.request.query_params.get("search", "")
        return PodCategory.objects.filter(name__icontains=query)