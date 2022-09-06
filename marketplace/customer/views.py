from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import AllProductsSerializer, CartSerializer

from api.models import Product
from .models import Cart
    
    
class AllProductsViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class CartsViewSet(ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

