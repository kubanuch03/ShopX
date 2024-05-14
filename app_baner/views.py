from rest_framework import generics, permissions, response, status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


from.models import Baner
from .serializers import BanerSerializer

# User Permissions
class BanerListView(APIView):
    def get(self, request):
        queryset = Baner.objects.all()
        serializer = BanerSerializer(queryset, many=True)
        return response.Response(serializer.data)



class BanerDetailView(generics.RetrieveAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        baner_id = self.kwargs.get('pk')
        return get_object_or_404(self.queryset, pk=baner_id)



# Admin Permissions



class BanerCreateView(generics.CreateAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.IsAdminUser]



class BanerUpdateView(generics.UpdateAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        baner_id = self.kwargs.get('pk')
        return get_object_or_404(self.queryset, pk=baner_id)

class BanerDeleteView(generics.DestroyAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        baner_id = self.kwargs.get('pk')
        instance = get_object_or_404(self.queryset, pk=baner_id)
        self.perform_destroy(instance)
        return response.Response({"success": f"Банер id: {baner_id} успешно удалена!"}, status=status.HTTP_200_OK)