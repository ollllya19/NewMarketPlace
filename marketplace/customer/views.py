from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework .permissions import IsAuthenticated
from .serializers import AllProductsSerializer, CartSerializer, CartCreateSerializer

from api.models import Product
from .models import Cart
    
    
class AllProductsViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class CartsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        cart_item = Cart(
            product=Product.objects.get(id=request.data['product']),
            col=request.data['col'],
            user=request.user)
        cart_item.save()
        serializer = CartCreateSerializer(cart_item)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        cart_item = Cart.objects.get(id=pk)
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)
    
    """
    
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
     
    """
