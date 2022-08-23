from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import AllProductsSerializer

from api.models import Product
    
    
class AllProductsViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer



