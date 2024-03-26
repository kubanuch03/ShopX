from rest_framework import generics, permissions, response, status


from.models import Baner
from .serializers import BanerSerializer

# User Permissions
class BanerListView(generics.ListAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.AllowAny]

class BanerDetailView(generics.RetrieveAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.AllowAny]


# Admin Permissions

class BanerCreateListView(generics.ListCreateAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.IsAdminUser]


class BanerUpdateView(generics.UpdateAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.IsAdminUser]



class BanerDeleteView(generics.DestroyAPIView):
    queryset = Baner.objects.all()
    serializer_class = BanerSerializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self,request,*args,**kwargs):
        baner_id = kwargs.get('pk')
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return response.Response({"success": f"Банер id: {baner_id} успешно удалена!"}, status=status.HTTP_200_OK)
        except:
            return response.Response({"error":f"Не удалось найти Банер id: {baner_id}"})