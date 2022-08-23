from rest_framework.viewsets import ModelViewSet

from api.serializers import ProductSerializer
from api.models import Product
from api.models import Farmer
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(farmer=Farmer.objects.get(id=3))
    serializer_class = ProductSerializer
