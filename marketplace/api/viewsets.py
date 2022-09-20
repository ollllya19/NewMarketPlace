from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework .permissions import IsAuthenticated

from api.serializers import ProductSerializer, ProductsFarmerSerializer, FarmerSerializer, PackageSerializer, PackageAcceptSerializer, PackagePackSerializer
from api.models import Product, Farmer, Package
    
    
class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        product = Product(
            title=request.data['title'],
            description=request.data['description'],
            price=request.data['price'],
            UOM=request.data['UOM'],
            user=request.user)
        product.save()
        serializer = ProductsFarmerSerializer(product)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({'delete': 'Object was deleted'})
        
    
class PackagesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        packages = Package.objects.filter(farmer=Farmer.objects.get(id=1))
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)
    

class PackageAcceptView(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageAcceptSerializer
    permission_classes = [IsAuthenticated]
    
    
class PackagePackView(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackagePackSerializer
    permission_classes = [IsAuthenticated]

        
# Farmer 
class FarmerProfileListCreateView(ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class FarmerProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated]
    