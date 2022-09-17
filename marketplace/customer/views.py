from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework .permissions import IsAuthenticated
from .serializers import AllProductsSerializer, CartSerializer

from api.models import Product
from .models import Cart
    
    
class AllProductsViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class CartsViewSet(ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

