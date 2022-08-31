from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework .permissions import IsAuthenticated

from api.serializers import ProductSerializer, FarmerSerializer, PackageSerializer, PackageAcceptSerializer, PackagePackSerializer
from api.models import Product, Farmer, Package
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    
class PackagesView(APIView):
    
    def get(self, request):
        packages = Package.objects.filter(farmer=Farmer.objects.get(id=1))
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)
    

class PackageAcceptView(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageAcceptSerializer
    
    
class PackagePackView(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackagePackSerializer
    
    
        
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
    