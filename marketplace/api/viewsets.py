from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework .permissions import IsAuthenticated

from api.serializers import ProductSerializer, FarmerSerializer
from api.models import Product
from api.models import Farmer
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    
# Farmer 
class FarmerProfileListCreateView(ListCreateAPIView):
    queryset=Farmer.objects.all()
    serializer_class=FarmerSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class FarmerProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Farmer.objects.all()
    serializer_class=FarmerSerializer
    permission_classes= [IsAuthenticated]
    